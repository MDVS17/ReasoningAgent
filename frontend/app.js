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
    role: "Directs the Microsoft 365 signal-to-blueprint factory loop.",
    detail:
      "The Master Agent studies simulated Microsoft 365 collaboration signals, decides which specialist should reason next, and keeps Syntrix focused on designing Copilot Agent Blueprints rather than generic automation ideas.",
    points: [
      "Routes Microsoft 365-style signals to the right specialist.",
      "Keeps pattern intelligence, blueprint generation, governance, and readiness in sequence.",
      "Combines impact scores, safety findings, and deployment readiness into one artifact.",
    ],
    icon: "core",
    master: true,
  },
  {
    name: "Signal Discovery Agent",
    tag: "Sensing",
    role: "Finds recurring Microsoft 365-style signals inside the selected workspace view.",
    detail:
      "This agent reviews simulated Microsoft 365 collaboration signals and extracts repeated behaviors that can become a Copilot Agent Blueprint.",
    points: [
      "Groups interactions by workflow and role context.",
      "Separates one-off questions from repeated work patterns.",
      "Feeds high-signal clusters into Pattern Intelligence.",
    ],
    icon: "signal",
  },
  {
    name: "Pattern Scoring Agent",
    tag: "Ranking",
    role: "Ranks repeated effort using Impact Score, ROI, and Confidence Score signals.",
    detail:
      "This agent evaluates frequency, time saved, repetition, business value, and risk so Syntrix can prioritize blueprint generation for the highest-impact Copilot Agent candidates.",
    points: [
      "Scores business impact with transparent local heuristics.",
      "Balances productivity lift with governance risk.",
      "Promotes the strongest patterns into Copilot Agent Blueprint Generation.",
    ],
    icon: "score",
  },
  {
    name: "Blueprint Architect Agent",
    tag: "Design",
    role: "Turns ranked patterns into a review-ready Copilot Agent Blueprint.",
    detail:
      "This agent converts the highest-value workflow pattern into a structured Copilot Agent Blueprint with purpose, triggers, instructions, tools, tests, and approval points for Copilot Studio review.",
    points: [
      "Creates instructions tied to the selected user's work.",
      "Specifies knowledge sources and suggested actions.",
      "Defines evaluation tests and deployment readiness checks before review.",
    ],
    icon: "blueprint",
  },
  {
    name: "Safety Governance Agent",
    tag: "Control",
    role: "Applies governance gates before the blueprint is trusted.",
    detail:
      "This agent checks whether the blueprint is appropriate for a synthetic local demo and ensures consequential actions stay behind human approval.",
    points: [
      "Validates synthetic-data boundaries.",
      "Adds human approval gates for sensitive actions.",
      "Keeps blueprint actions advisory until a human approves sensitive actions.",
    ],
    icon: "shield",
  },
  {
    name: "Learning Loop Agent",
    tag: "Improve",
    role: "Prepares controlled blueprint updates as new Microsoft 365-style signals appear.",
    detail:
      "This agent closes the loop by comparing Week 1 and Week 3 signals, identifying where the Copilot Agent Blueprint should improve, narrow, or add new tests.",
    points: [
      "Tracks Impact Score and Confidence Score movement over time.",
      "Suggests trigger and evaluation refinements.",
      "Turns observed signal changes into safer future blueprint versions.",
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

function escapeHtml(value = "") {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function listItems(items = []) {
  const values = Array.isArray(items) ? items : [items].filter(Boolean);
  return values.map((item) => `<li>${escapeHtml(item)}</li>`).join("");
}

function setText(id, value, fallback = "Not specified") {
  const element = $(id);
  if (element) {
    element.textContent = value ?? fallback;
  }
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
  const blueprint = payload.copilot_agent_blueprint || payload.blueprint || payload.recommended_blueprint || {};
  const opportunity = payload.opportunity || (payload.opportunity_scores || [])[0] || {};
  const impactScore = blueprint.impact_score ?? opportunity.syntrix_opportunity_score ?? "--";
  setText("blueprintName", blueprint.agent_name, "Copilot Agent Blueprint");
  setText("blueprintTarget", `Target user: ${blueprint.target_user || "Workspace owner"}`);
  setText("artifactScore", `Impact Score ${impactScore}`);
  setText("blueprintPurpose", blueprint.purpose, "Review-ready Copilot Agent Blueprint generated from simulated Microsoft 365 collaboration signals.");
  setText("blueprintDepartment", blueprint.department || blueprint.target_user);
  setText("blueprintHoursSaved", blueprint.estimated_hours_saved ? `${blueprint.estimated_hours_saved} hrs/year` : "--");
  setText("blueprintRoi", blueprint.estimated_annual_roi || "--");
  setText("blueprintConfidence", blueprint.confidence_score ? `${blueprint.confidence_score}/100` : "--");
  setText("blueprintImpact", impactScore === "--" ? "--" : `${impactScore}/100`);
  setText("blueprintReadiness", blueprint.deployment_readiness, "Ready for Copilot Studio Review after governance review");
  setText(
    "blueprintProblem",
    blueprint.business_problem || opportunity.rationale,
    "Generated by the Syntrix Agent Factory from repeated Microsoft 365-style signals.",
  );
  setText(
    "blueprintPattern",
    blueprint.detected_work_pattern || (blueprint.triggering_work_patterns || [])[0],
    "Repeated work pattern detected from the Graph-ready signal model.",
  );
  $("blueprintSignals").innerHTML = listItems(
    blueprint.microsoft_365_signals_used || [
      "Outlook: repeated follow-up emails and recurring status requests",
      "Teams: repeated project updates and blocked-task discussions",
      "Calendar: recurring preparation and follow-up loops",
      "SharePoint/OneDrive: repeated document access and reporting packs",
      "Planner: recurring tasks, overdue work, and handoff patterns",
    ],
  );
  $("blueprintKnowledge").innerHTML = listItems(blueprint.suggested_knowledge_sources || blueprint.required_knowledge_sources);
  $("blueprintActions").innerHTML = listItems(blueprint.suggested_actions || blueprint.suggested_tools_actions);
  $("blueprintInstructions").innerHTML = listItems(blueprint.system_instructions || blueprint.instructions);
  $("blueprintGuardrails").innerHTML = listItems(blueprint.guardrails);
  $("blueprintTests").innerHTML = listItems(blueprint.evaluation_tests);
  $("approvalGates").innerHTML = listItems(blueprint.human_approval_points);
  $("blueprintGrounding").innerHTML = listItems(blueprint.foundry_iq_grounding || blueprint.grounded_sources);
  setText("blueprintReviewNotes", blueprint.copilot_studio_review_notes, "Copilot Studio review-ready blueprint; no live runtime integration is claimed.");
  setText("blueprintImprovement", blueprint.continuous_improvement_recommendation);
  $("riskBadge").textContent = `${payload.safety_review?.risk_level || "Controlled"} risk workflow`;
  renderGovernanceGates(payload.governance_gates);
}

function renderGovernanceGates(governanceGates) {
  const gates = governanceGates || [
    { gate: "Human approval before external communication" },
    { gate: "Human approval before system changes" },
    { gate: "Source traceability required" },
    { gate: "Sensitive content flagged" },
    { gate: "No autonomous write actions without approval" },
  ];
  $("governanceGates").innerHTML = gates
    .map(
      (gate) => `
        <div class="gate-item">
          <span></span>
          <div>
            <strong>${gate.gate}</strong>
            ${gate.reason ? `<small>${gate.reason}</small>` : ""}
          </div>
        </div>
      `,
    )
    .join("");
}

function renderIQCards(iq) {
  const cards = [
    {
      name: "Foundry IQ",
      description: "Live-verified Foundry IQ grounding with cited synthetic governance sources.",
      signals: iq.foundry_iq.signals,
      status: "Live verified",
    },
    {
      name: "Fabric IQ",
      description: "Semantic ontology layer for users, workflows, agents, and guardrails.",
      signals: iq.fabric_iq.signals,
      status: "Semantic ontology",
    },
    {
      name: "Work IQ",
      description: "Microsoft 365-style synthetic work-context signals.",
      signals: iq.work_iq.signals,
      status: "Synthetic work signals",
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
            <span>${card.status || "local demo"}</span>
          </div>
          <h3>Ready layer</h3>
          <p>${card.description}</p>
          ${signalMarkup}
        </article>
      `;
    })
    .join("");
}

function renderIQEvidence(data) {
  const evidence = data.iq_evidence || {};
  const blueprint = data.copilot_agent_blueprint || data.recommended_blueprint || {};
  const citations = blueprint.citations || evidence.citations || [];
  const items = evidence.evidence || [];
  $("citationCount").textContent = `${citations.length} citations`;
  $("iqEvidenceSummary").textContent =
    blueprint.evidence_summary ||
    evidence.evidence_summary ||
    "Blueprint evidence will appear after Microsoft 365-style signals are analyzed.";
  $("iqEvidenceList").innerHTML = items
    .slice(0, 5)
    .map(
      (item) => {
        const sourceName = item.source_name || "Synthetic source";
        return `
        <div class="citation-item">
          <span>${escapeHtml(item.layer || "IQ Layer")}</span>
          <strong title="${escapeHtml(sourceName)}">${escapeHtml(sourceName)}</strong>
          <p>${escapeHtml(item.snippet || "")}</p>
        </div>
      `;
      },
    )
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
          <div class="line-row-top">
            <span title="${row.workflow}">${truncate(row.workflow, 28)}</span>
            <strong>${row.week_1_avg_score} -> ${row.week_3_avg_score}</strong>
          </div>
          <div class="score-line" style="--week-one:${weekOne}%; --week-three:${weekThree}%"></div>
        </div>
      `;
    })
    .join("");
}

function renderReasoningEngine(data) {
  const summary = data.master_agent_summary;
  const trace = data.reasoning_trace || [];
  if (!summary) {
    return;
  }

  $("traceCount").textContent = `${trace.length} handoffs`;
  $("masterRecommendation").textContent = summary.top_recommendation;
  $("masterDecision").textContent = summary.orchestration_decision;
  $("reasoningTrace").innerHTML = trace
    .map(
      (step) => `
        <div class="trace-item">
          <span>${step.step}</span>
          <div>
            <strong>${step.agent}</strong>
            <p>${step.decision}</p>
            <small>Handoff: ${step.handoff_to}</small>
          </div>
        </div>
      `,
    )
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
  renderBars($("scoreChart"), data.opportunity_scores || data.opportunities, "syntrix_opportunity_score", maxScore);
  renderFlow(data.reasoning_flow);
  renderImprovement(data.week_comparison);
  if (data.learning_loop_recommendation) {
    $("confidenceLift").textContent = `+${data.learning_loop_recommendation.confidence_lift} pts`;
    $("learningCapability").textContent = data.learning_loop_recommendation.new_capability;
  }
  renderReasoningEngine(data);
  renderIQEvidence(data);
}

async function loadProfiles() {
  const payload = await api("/api/profiles");
  const labels = {
    "All roles": "All Microsoft 365 signals",
    "Marketing Manager": "Marketing signal model",
    "Project Manager": "Delivery operations signal model",
    "HR Business Partner": "People advisory signal model",
  };
  const options = [{ profile: "All roles" }, ...payload.data];
  $("profileSelect").innerHTML = options
    .map((item) => `<option value="${item.profile}">${labels[item.profile] || item.profile}</option>`)
    .join("");
}

async function refreshDemo() {
  state.profile = $("profileSelect").value || "All roles";
  const [analysisPayload, iqPayload, evalPayload] = await Promise.all([
    api("/api/analyze", { method: "POST", body: JSON.stringify({ profile: state.profile }) }),
    api("/api/iq/status"),
    api("/api/evaluation/summary"),
  ]);

  state.analysis = analysisPayload.data;
  state.blueprint = analysisPayload.data;
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
