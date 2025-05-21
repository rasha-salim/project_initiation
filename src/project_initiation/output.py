from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any    
# :Optional[str] = None  # To make fields optional
# Define models for tables and nested structures
class SmartGoal(BaseModel):
    goal: str = Field(..., description="Goal name")
    specific: str = Field(..., description="Specific details")
    measurable: str = Field(..., description="Metrics to measure success")
    achievable: str = Field(..., description="Feasibility assessment")
    relevant: str = Field(..., description="Alignment with objectives")
    time_bound: str = Field(..., description="Deadline or timeframe")

class TechnicalChallenge(BaseModel):
    challenge: str = Field(..., description="Technical challenge description")
    proposed_solution: str = Field(..., description="Proposed solution")
    impact: str = Field(..., description="Impact description")

class TeamRole(BaseModel):
    role: str = Field(..., description="Team role title")
    responsibilities: str = Field(..., description="Key responsibilities")
    required_skills: str = Field(..., description="Required skills")
    allocation: str = Field(..., description="Full/Part time allocation")

class Phase(BaseModel):
    phase: str = Field(..., description="Phase name")
    start_date: str = Field(..., description="Start date")
    end_date: str = Field(..., description="End date")
    duration: str = Field(..., description="Duration")

class Milestone(BaseModel):
    milestone: str = Field(..., description="Milestone name")
    description: str = Field(..., description="Description")
    target_date: str = Field(..., description="Target date")
    dependencies: str = Field(..., description="Dependencies")

#class CostCategory(BaseModel):
    #category: str = Field(..., description="Cost category")
    #description: str = Field(..., description="Description")
    #estimated_cost: str = Field(..., description="Estimated cost")

#class BudgetScenario(BaseModel):
    #scenario: str = Field(..., description="Budget scenario (Optimistic/Realistic/Pessimistic)")
    #total_cost: str = Field(..., description="Total cost")
    #key_assumptions: str = Field(..., description="Key assumptions")
    #impact: str = Field(..., description="Impact")

class Risk(BaseModel):
    risk: str = Field(..., description="Risk description")
    probability: str = Field(..., description="Probability (H/M/L)")
    impact: str = Field(..., description="Impact (H/M/L)")
    risk_score: str = Field(..., description="Risk score")
    mitigation_strategy: str = Field(..., description="Mitigation strategy")

#class Stakeholder(BaseModel):
    #stakeholder: str = Field(..., description="Stakeholder name")
    #role: str = Field(..., description="Stakeholder role")
    #date: Optional[str] = Field(None, description="Sign-off date")
    #signature: Optional[str] = Field(None, description="Signature")

#class GlossaryTerm(BaseModel):
    term: str = Field(..., description="Term")
    definition: str = Field(..., description="Definition")

# Section models
class ExecutiveSummary(BaseModel):
    content: str = Field(..., description="Executive summary content")

class ProjectObjectives(BaseModel):
    primary_business_objectives: str = Field(..., description="Primary business objectives")
    smart_goals: List[SmartGoal] = Field(..., description="SMART goals")
    success_criteria_and_kpis: str = Field(..., description="Success criteria and KPIs")

#class ExpectedBenefits(BaseModel):
    #quantitative_benefits: List[str] = Field(..., description="Quantitative benefits")
    #qualitative_benefits: List[str] = Field(..., description="Qualitative benefits")

class ProjectJustification(BaseModel):
    business_case_summary: str = Field(..., description="Business case summary")
    #expected_benefits: ExpectedBenefits = Field(..., description="Expected benefits")
    strategic_alignment: str = Field(..., description="Strategic alignment")
    roi_projections: str = Field(..., description="ROI projections")

class ScopeInScope(BaseModel):
    features_and_deliverables: List[str] = Field(..., description="Features and deliverables")
    functional_requirements: List[str] = Field(..., description="Functional requirements")
    non_functional_requirements: List[str] = Field(..., description="Non-functional requirements")

class ScopeDefinition(BaseModel):
    in_scope: ScopeInScope = Field(..., description="In scope items")
    #out_of_scope: List[str] = Field(..., description="Out of scope items")
    minimum_viable_product: str = Field(..., description="Minimum viable product")
    future_phases: str = Field(..., description="Future phases")

class Constraints(BaseModel):
    budget_constraints: str = Field(..., description="Budget constraints")
    timeline_constraints: str = Field(..., description="Timeline constraints")
    technical_constraints: str = Field(..., description="Technical constraints")
    resource_constraints: str = Field(..., description="Resource constraints")
    #regulatory_compliance_constraints: str = Field(..., description="Regulatory/compliance constraints")

class AssumptionsAndConstraints(BaseModel):
    key_assumptions: List[str] = Field(..., description="Key assumptions")
    constraints: Constraints = Field(..., description="Constraints")

class TechnicalImplementation(BaseModel):
    technology_stack: str = Field(..., description="Technology stack")
    architecture_overview: str = Field(..., description="Architecture overview")
    integration_requirements: str = Field(..., description="Integration requirements")
    technical_challenges_and_solutions: List[TechnicalChallenge] = Field(..., description="Technical challenges and solutions")
    security_and_compliance: str = Field(..., description="Security and compliance")  

#class TeamStructureAndResources(BaseModel):
    #required_roles_and_responsibilities: List[TeamRole] = Field(..., description="Required roles and responsibilities")
    #external_resources: str = Field(..., description="External resources")

#class TimelineAndMilestones(BaseModel):
    #high_level_schedule: List[Phase] = Field(..., description="High-level schedule")
    #key_milestones: List[Milestone] = Field(..., description="Key milestones")
    #dependencies: str = Field(..., description="Dependencies")

#class BudgetProjection(BaseModel):
    #cost_breakdown: List[CostCategory] = Field(..., description="Cost breakdown")
    #budget_scenarios: List[BudgetScenario] = Field(..., description="Budget scenarios")
    #cost_saving_opportunities: str = Field(..., description="Cost-saving opportunities")

class RiskAssessment(BaseModel):
    key_risks: List[Risk] = Field(..., description="Key risks")
    contingency_plans: str = Field(..., description="Contingency plans")

#class ApprovalAndSignOff(BaseModel):
    #key_stakeholders: List[Stakeholder] = Field(..., description="Key stakeholders")
    #change_management_process: str = Field(..., description="Change management process")

#class Appendices(BaseModel):
    #supporting_documentation: str = Field(..., description="Supporting documentation")
    #glossary: List[GlossaryTerm] = Field(..., description="Glossary")

#class DocumentControl(BaseModel):
   # version: str = Field(..., description="Document version")
    #last_updated: str = Field(..., description="Last updated date")
   # prepared_by: str = Field(..., description="Prepared by")
    #approved_by: str = Field(..., description="Approved by")

# Main Project Scope Document model
class ProjectScopeDocument(BaseModel):
    executive_summary: ExecutiveSummary = Field(..., description="Executive Summary")
    project_objectives: ProjectObjectives = Field(..., description="Project Objectives")
    project_justification: ProjectJustification = Field(..., description="Project Justification")
    scope_definition: ScopeDefinition = Field(..., description="Scope Definition")
    assumptions_and_constraints: AssumptionsAndConstraints = Field(..., description="Assumptions and Constraints")
    technical_implementation: TechnicalImplementation = Field(..., description="Technical Implementation")
    #team_structure_and_resources: TeamStructureAndResources = Field(..., description="Team Structure and Resources")
    #timeline_and_milestones: TimelineAndMilestones = Field(..., description="Timeline and Milestones")
    #budget_projection: BudgetProjection = Field(..., description="Budget Projection")
    risk_assessment: RiskAssessment = Field(..., description="Risk Assessment")
    #approval_and_sign_off: ApprovalAndSignOff = Field(..., description="Approval and Sign-off")
    #appendices: Appendices = Field(..., description="Appendices")
    #document_control: DocumentControl = Field(..., description="Document Control")
    class Config:
        extra = "ignore"  # Ignore extra fields not in the model


# For Roadmap
# Models for structured data (tables and prioritized features)
class Feature(BaseModel):
    name: str = Field(description="Feature name")
    description: Optional[str] = Field(None, description="Feature description")

class PrioritizedFeatures(BaseModel):
    must_have: List[Feature] = Field(description="Critical features for launch")
    should_have: List[Feature] = Field(description="Important but not blocking features")
    could_have: List[Feature] = Field(description="Desired enhancement features")

class TimelinePhase(BaseModel):
    phase: str = Field(description="Phase name")
    timeframe: str = Field(description="Timeframe for the phase")
    deliverables: str = Field(description="Deliverables for the phase")
    owner: Optional[str] = Field(None, description="Owner of the phase")

class Risk(BaseModel):
    risk: str = Field(description="Risk description")
    impact: str = Field(description="High/Med/Low")
    likelihood: str = Field(description="High/Med/Low")
    mitigation: str = Field(description="Mitigation strategy")

class Decision(BaseModel):
    date: str = Field(description="Decision date")
    decision: str = Field(description="Decision made")
    rationale: str = Field(description="Rationale for decision")
    alternatives_considered: Optional[str] = Field(None, description="Alternatives considered")

# Main Product Roadmap model
class ProductRoadmap(BaseModel):
    # Executive Summary
    executive_summary: str = Field(description="One paragraph overview of the product")
    
    # Product Vision
    problem_statement: str = Field(description="What problem are we solving?")
    strategic_alignment: str = Field(description="How does this align with company strategy?")
    one_year_vision: str = Field(description="What does success look like in 1 year?")
    
    # Target Users
    primary_user_persona: str = Field(description="Primary user persona")
    key_user_needs: List[str] = Field(description="Key user needs")
    needs_validation_method: str = Field(description="How we validate these needs")
    
    # Core Features
    features: PrioritizedFeatures = Field(description="Prioritized features")
    
    # Timeline
    timeline: List[TimelinePhase] = Field(description="Project timeline by phase")
    
    # Resource Requirements
    team_composition: List[str] = Field(description="Team composition")
    budget: str = Field(description="Budget requirements")
    tools_technologies: List[str] = Field(description="Tools and technologies needed")
    
    # Success Metrics
    primary_kpi: str = Field(description="Primary KPI")
    secondary_metrics: List[str] = Field(description="Secondary metrics")
    data_collection_method: str = Field(description="Data collection method")
    
    # Risks & Mitigation
    risks: List[Risk] = Field(description="Risks and mitigation strategies")
    
    # Decision Log
    decisions: List[Decision] = Field(description="Decision log")
    
    # Next Steps
    immediate_actions: List[str] = Field(description="Immediate actions for next 2 weeks")
    #stakeholder_approvals: List[str] = Field(description="Key stakeholder approvals needed")
    open_questions: List[str] = Field(description="Open questions to resolve")