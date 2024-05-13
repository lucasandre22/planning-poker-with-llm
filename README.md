# Prompt to generate tickets:
"""
Help me generate fake data about a agile team that works with Jira.
This data will be all the tickets that this team worked previously.
The jira tikcket is called METHODS-X with X being the number of the ticket.
Generate json data, one per line, organized like json lines file.
The json should be estructured like this example:

{"METHODS-1": {"summary": "", "description": "", "components": ["", ""], "labels": [""], "type": "", "priority": "", "story_points": 0}}

Here are some explanation for each field:
Explanation for the "summary" field:
    A summary of what the issue is about, a short phrase to give you an idea of what the issue is about.

Explanation for the "description" field:
    Literally, a description of the issue. Please, simulate this field with detailed descriptions and other not so detailed.

Possible values for "components" field:
    "frontend react"
    "frontend angular"
    "backend node.js"
    "backend python"
    "mobile ios"
    "mobile android"
    "testing automated"
    "testing manual"
    "documentation"
    "devops docker"
    "devops kubernetes"
    "security encryption"
    "security authentication"
    "analytics tracking"
    "integration third-party"
    "deployment AWS"
    "deployment Azure"
    "deployment Google Cloud"
    "performance monitoring"
    "UI/UX design"
    "data migration"
    "data analysis"
    "support"
    "training"

Possible values for "labels" field:
    "backend"
    "frontend"
    "database"
    "security"
    "authentication"
    "authorization"
    "performance"
    "optimization"
    "bug"
    "feature"
    "enhancement"
    "documentation"
    "user-interface"
    "user-experience"
    "testing"
    "deployment"
    "maintenance"
    "refactoring"
    "integration"
    "third-party"
    "workflow"

Possible values for "type" field:
    Bug: A bug is a problem which impairs or prevents the functions of a product.
    Story: A user story is the smallest unit of work that needs to be done.
    Task: A task represents work that needs to be done.
    Improvement: A improvement represents new features added to a product or component that the team develops.

Possible values for "priority" field:
    Low: Minor problem easily worked around.
    Medium: has the potential to affect progress.
    High: Serious problem that could block progress.
    Highest: the problem will block progress.

Possible values for story_points field:
    Story Points are units of measurement that you use to define the complexity of a user story. It follows fibonacci numbers.


"""