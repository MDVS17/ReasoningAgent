const state = {
  profile: "All roles",
  analysis: null,
  blueprint: null,
  iq: null,
  evaluation: null,
};

const $ = (id) => document.getElementById(id);

async function api(path, options = {}) {
  const response = await fetch(path, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  if (!response.ok) {
    throw new Error(`API request failed: ${path}`);
  }
  return response.json();
}

function truncate(text, max = 34) {
  return text.length > max ? `${text.slice(0, max - 1)}...` : text;
}

function renderBars(container, rows, valueKey, maxValue, colorClass = "") {
  container.innerHTML = "";
  rows.slice(0, 8).forEach((row) => {
    const value = Number(row[valueKey]);
    const width = Math.max(4, Math.round((value / maxValue) * 100));
    const el = document.createElement("div");
    el.className = "bar-row";
    el.innerHTML = `
      <span title="${row.workflow}">${truncate(row.workflow)}</span>
      <div class="bar-track"><div class="bar-fill ${colorClass}" style="width:${width}%"></div></div>
      <strong>${value.toFixed(value % 1 ? 1 : 0)}</strong>
    `;
    container.appendChild(el);
  });
}

function renderFlow(steps) {
  $("reasoningFlow").innerHTML = steps
    .map((step, index) => `<div class="flow-step"><span>${index + 1}</span><strong>${step}</strong></div>`)
    .join("");
}

function renderBlueprint(payload) {
  const blueprint = payload.blueprint;
  const review = payload.safety_review;
  $("blueprintName").textContent = blueprint.agent_name;
  $("blueprintTarget").textContent = blueprint.target_user;
  $("blueprintPurpose").textContent = blueprint.purpose;
  $("blueprintInstructions").innerHTML = blueprint.instructions.map((item) => `<li>${item}</li>`).join("");
  $("blueprintGuardrails").innerHTML = blueprint.guardrails.map((item) => `<li>${item}</li>`).join("");
  $("safetyDecision").textContent = review.decision;
  $("riskBadge").textContent = `${review.risk_level} risk`;
  $("safetyNotes").textContent = review.reviewer_notes;
  $("approvalPoints").innerHTML = blueprint.human_approval_points.map((item) => `<li>${item}</li>`).join("");
}

function renderIQCards(iq) {
  const cards = [iq.foundry_iq, iq.fabric_iq, iq.work_iq];
  $("iqCards").innerHTML = cards
    .map((card) => {
      const signalMarkup = (card.signals || [])
        .map((signal) => {
          const value = signal.score ?? signal.value;
          return `<div class="eval-item"><span>${signal.label}</span><strong>${value}</strong></div>`;
        })
        .join("");
      return `
        <article class="iq-card">
          <strong>${card.name}</strong>
          <h3>${card.status}</h3>
          <p>${card.description}</p>
          ${signalMarkup}
        </article>
      `;
    })
    .join("");
}

function renderImprovement(rows) {
  $("improvementChart").innerHTML = rows
    .slice(0, 8)
    .map((row) => {
      const weekOne = Math.max(0, Math.min(94, Number(row.week_1_avg_score)));
      const weekThree = Math.max(0, Math.min(94, Number(row.week_3_avg_score)));
      return `
        <div class="line-row">
          <span title="${row.workflow}">${truncate(row.workflow, 28)}</span>
          <div class="score-line" style="--week-one:${weekOne}%; --week-three:${weekThree}%"></div>
          <strong>${row.week_1_avg_score} -> ${row.week_3_avg_score}</strong>
        </div>
      `;
    })
    .join("");
}

function renderEvaluation(summary) {
  $("evalStatus").textContent = summary.safety_status;
  $("evalList").innerHTML = summary.rubric
    .map((item) => `<div class="eval-item"><span>${item.criterion}</span><strong>${item.score}</strong></div>`)
    .join("");
}

function renderAnalysis() {
  const data = state.analysis;
  $("metricInteractions").textContent = data.summary.interaction_count;
  $("metricWorkflows").textContent = data.summary.workflow_count;
  $("metricTopScore").textContent = data.summary.top_opportunity_score ?? "--";

  const maxFrequency = Math.max(...data.task_frequency.map((row) => Number(row.count)), 1);
  renderBars($("frequencyChart"), data.task_frequency, "count", maxFrequency);

  const maxScore = 100;
  renderBars($("scoreChart"), data.opportunities, "syntrix_opportunity_score", maxScore);
  renderFlow(data.reasoning_flow);
  renderImprovement(data.week_comparison);
}

async function loadProfiles() {
  const payload = await api("/api/profiles");
  const options = [{ profile: "All roles" }, ...payload.data];
  $("profileSelect").innerHTML = options.map((item) => `<option>${item.profile}</option>`).join("");
}

async function refreshDemo() {
  state.profile = $("profileSelect").value || "All roles";
  const [analysisPayload, blueprintPayload, iqPayload, evalPayload] = await Promise.all([
    api("/api/analyze", { method: "POST", body: JSON.stringify({ profile: state.profile }) }),
    api("/api/blueprint", { method: "POST", body: JSON.stringify({ profile: state.profile }) }),
    api("/api/iq/status"),
    api("/api/evaluation/summary"),
  ]);

  state.analysis = analysisPayload.data;
  state.blueprint = blueprintPayload.data;
  state.iq = iqPayload.data;
  state.evaluation = evalPayload.data;

  renderAnalysis();
  renderBlueprint(state.blueprint);
  renderIQCards(state.iq);
  renderEvaluation(state.evaluation);
}

async function boot() {
  try {
    await loadProfiles();
    $("profileSelect").addEventListener("change", refreshDemo);
    await refreshDemo();
  } catch (error) {
    document.body.insertAdjacentHTML(
      "afterbegin",
      `<div class="boundary-note" style="position:fixed;z-index:10;left:20px;right:20px;top:20px;">${error.message}</div>`,
    );
  }
}

boot();
