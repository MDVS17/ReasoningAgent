const state = {
  profile: "All roles",
  analysis: null,
  blueprint: null,
  iq: null,
  evaluation: null,
};

const $ = (id) => document.getElementById(id);

const masterAgentSystem = [
  {
    name: "Master Agent",
    tag: "Orchestrator",
    role: "Coordinates the full discovery-to-blueprint reasoning loop.",
    detail:
      "The Master Agent studies workspace signals, decides which specialized agent should reason next, and keeps the system focused on discovering useful personalized agents instead of producing generic automation ideas.",
    points: [
      "Routes work signals to the right specialist agent.",
      "Maintains the product goal: discover, design, and improve agents.",
      "Combines scores, safety findings, and blueprint recommendations.",
    ],
    icon: "core",
    master: true,
  },
  {
    name: "Signal Discovery Agent",
    tag: "Sensing",
    role: "Reads workspace signals and identifies recurring work themes.",
    detail:
      "This agent reviews synthetic Copilot-style interactions and extracts the repeated behaviors that suggest an agent opportunity may exist.",
    points: [
      "Groups prompts by workflow and role context.",
      "Separates one-off questions from repeated work patterns.",
      "Feeds high-signal clusters into scoring.",
    ],
    icon: "signal",
  },
  {
    name: "Pattern Scoring Agent",
    tag: "Ranking",
    role: "Turns repeated effort into a Syntrix Opportunity Score.",
    detail:
      "This agent evaluates frequency, time saved, repetition, business value, and risk so Syntrix can prioritize the agent opportunities most worth designing.",
    points: [
      "Scores opportunities with transparent local heuristics.",
      "Balances productivity lift with governance risk.",
      "Ranks the best opportunities for blueprint generation.",
    ],
    icon: "score",
  },
  {
    name: "Blueprint Architect Agent",
    tag: "Design",
    role: "Designs safe personalized agent blueprints from ranked patterns.",
    detail:
      "This agent converts the highest-value workflow pattern into a structured Syntrix Agent Blueprint with purpose, triggers, instructions, tools, tests, and approval points.",
    points: [
      "Creates instructions tied to the target user's work.",
      "Specifies knowledge sources and suggested actions.",
      "Defines evaluation tests before deployment.",
    ],
    icon: "blueprint",
  },
  {
    name: "Safety Governance Agent",
    tag: "Control",
    role: "Reviews proposed agents for policy, approval, and risk controls.",
    detail:
      "This agent checks whether the blueprint is appropriate for a synthetic local demo and ensures consequential actions stay behind human approval.",
    points: [
      "Validates synthetic-data boundaries.",
      "Adds human approval gates for sensitive actions.",
      "Keeps recommendations advisory until governed.",
    ],
    icon: "shield",
  },
  {
    name: "Learning Loop Agent",
    tag: "Improve",
    role: "Compares usage over time and recommends blueprint refinements.",
    detail:
      "This agent closes the loop by comparing Week 1 and Week 3 signals, identifying where the agent design should improve, narrow, or add new tests.",
    points: [
      "Tracks opportunity score movement over time.",
      "Suggests trigger and evaluation refinements.",
      "Turns demo feedback into better future agents.",
    ],
    icon: "loop",
  },
];

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

function avatar(icon) {
  const paths = {
    core: `<path d="M6 15h16v10H6z"/><path d="M10 9h8v6h-8z"/><path d="M12 5h4v4h-4z"/><path d="M9 18h2v2H9zM17 18h2v2h-2z"/>`,
    signal: `<path d="M5 23h4v4H5zM12 17h4v10h-4zM19 11h4v16h-4z"/><path d="M7 11l5-5 5 4 6-7"/>`,
    score: `<path d="M5 24h18"/><path d="M7 20l4-5 4 3 7-10"/><path d="M18 8h4v4"/>`,
    blueprint: `<path d="M7 5h16v22H7z"/><path d="M11 10h8M11 15h8M11 20h5"/>`,
    shield: `<path d="M16 4l10 4v7c0 7-4.5 11-10 13C10.5 26 6 22 6 15V8z"/><path d="M12 16l3 3 6-7"/>`,
    loop: `<path d="M8 12a8 8 0 0113-4l2 2"/><path d="M23 5v5h-5"/><path d="M24 20a8 8 0 01-13 4l-2-2"/><path d="M9 27v-5h5"/>`,
  };
  return `
    <svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round" aria-hidden="true">
      ${paths[icon] || paths.core}
    </svg>
  `;
}

function renderAgentDetail(agent) {
  $("agentDetailPanel").innerHTML = `
    <div class="agent-avatar">${avatar(agent.icon)}</div>
    <span class="agent-tag">${agent.tag}</span>
    <h3>${agent.name}</h3>
    <p>${agent.detail}</p>
    <ul>
      ${agent.points.map((point) => `<li>${point}</li>`).join("")}
    </ul>
  `;
}

function renderFlow() {
  $("reasoningFlow").innerHTML = masterAgentSystem
    .map(
      (agent, index) => `
        <button class="agent-card ${agent.master ? "is-master is-active" : ""}" type="button" data-agent-index="${index}">
          <div class="agent-card-header">
            <div class="agent-avatar">${avatar(agent.icon)}</div>
            <div>
              <span class="agent-tag">${agent.tag}</span>
              <h3>${agent.name}</h3>
            </div>
          </div>
          <p>${agent.role}</p>
        </button>
      `,
    )
    .join("");

  renderAgentDetail(masterAgentSystem[0]);

  document.querySelectorAll(".agent-card").forEach((card) => {
    card.addEventListener("click", () => {
      const index = Number(card.dataset.agentIndex);
      document.querySelectorAll(".agent-card").forEach((item) => item.classList.remove("is-active"));
      card.classList.add("is-active");
      renderAgentDetail(masterAgentSystem[index]);
    });
  });
}

function renderBlueprint(payload) {
  const blueprint = payload.blueprint;
  const opportunity = payload.opportunity;
  $("blueprintName").textContent = blueprint.agent_name;
  $("blueprintTarget").textContent = `Target user: ${blueprint.target_user}`;
  $("artifactScore").textContent = `Score ${opportunity.syntrix_opportunity_score}`;
  $("blueprintPurpose").textContent = blueprint.purpose;
  $("blueprintRationale").textContent = opportunity.rationale;
  $("blueprintTriggers").innerHTML = blueprint.triggering_work_patterns.map((item) => `<li>${item}</li>`).join("");
  $("blueprintCapabilities").innerHTML = blueprint.suggested_tools_actions.map((item) => `<li>${item}</li>`).join("");
  $("blueprintGuardrails").innerHTML = blueprint.guardrails.map((item) => `<li>${item}</li>`).join("");
  $("approvalGates").innerHTML = blueprint.human_approval_points.map((item) => `<li>${item}</li>`).join("");
  $("blueprintImprovement").textContent = blueprint.continuous_improvement_recommendation;
  $("riskBadge").textContent = `${payload.safety_review.risk_level} risk workflow`;
  renderGovernanceGates();
}

function renderGovernanceGates() {
  const gates = [
    "Human approval before external communication",
    "Human approval before system changes",
    "Source traceability required",
    "Sensitive content flagged",
    "No autonomous write actions without approval",
  ];
  $("governanceGates").innerHTML = gates
    .map(
      (gate) => `
        <div class="gate-item">
          <span></span>
          <strong>${gate}</strong>
        </div>
      `,
    )
    .join("");
}

function renderIQCards(iq) {
  const cards = [
    {
      name: "Foundry IQ",
      description: "Grounded knowledge retrieval for approved sources.",
      signals: iq.foundry_iq.signals,
    },
    {
      name: "Fabric IQ",
      description: "Semantic model for users, workflows, agents, and guardrails.",
      signals: iq.fabric_iq.signals,
    },
    {
      name: "Work IQ",
      description: "Work-context signals from collaboration patterns and user activity.",
      signals: iq.work_iq.signals,
    },
  ];
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
          <div class="iq-card-heading">
            <strong>${card.name}</strong>
            <span>demo mode</span>
          </div>
          <h3>Ready layer</h3>
          <p>${card.description}</p>
          ${signalMarkup}
        </article>
      `;
    })
    .join("");
}

function renderImprovement(rows) {
  if (rows.length) {
    const first = rows[0];
    const lift = Number(first.week_3_avg_score) - Number(first.week_1_avg_score);
    $("confidenceLift").textContent = `+${lift} pts`;
    $("learningCapability").textContent = `${first.workflow} escalation summary`;
  }
  $("improvementChart").innerHTML = rows
    .slice(0, 5)
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
  state.evaluation = summary;
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
  const labels = {
    "All roles": "All workspace signals",
    "Marketing Manager": "Marketing launch workspace",
    "Project Manager": "Delivery operations workspace",
    "HR Business Partner": "People advisory workspace",
  };
  const options = [{ profile: "All roles" }, ...payload.data];
  $("profileSelect").innerHTML = options
    .map((item) => `<option value="${item.profile}">${labels[item.profile] || item.profile}</option>`)
    .join("");
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
