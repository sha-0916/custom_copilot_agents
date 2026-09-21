# custom_copilot_agents

A collection of custom [GitHub Copilot agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents) (`.agent.md` files) for use in VS Code.

## Agents

| Agent | Description |
|-------|-------------|
| [readme-specialist](.github/agents/readme-specialist.agent.md) | Improves README structure and clarity while verifying every command, path, and feature claim against the actual repository contents. |

## Usage

1. Copy the desired `.agent.md` file from [.github/agents](.github/agents) into your own repository's `.github/agents/` folder (or your user profile's `agents/` folder for cross-workspace use).
2. Select the agent from the agent picker in VS Code Copilot Chat, or let another agent delegate to it as a subagent based on its description.

