const fs = require('fs-extra');
const path = require('node:path');
const chalk = require('chalk');

/**
 * Claude Code specific configuration for CPM
 */
async function install(options) {
  const { projectRoot, config, logger } = options;

  try {
    logger.log(chalk.blue('Configuring CPM for Claude Code...'));

    // Claude Code uses CLAUDE.md for project instructions
    // CPM adds cinematic production context to the project

    const claudeMdPath = path.join(projectRoot, 'CLAUDE.md');

    if (await fs.pathExists(claudeMdPath)) {
      // Append CPM instructions if CLAUDE.md exists
      const existingContent = await fs.readFile(claudeMdPath, 'utf-8');

      if (!existingContent.includes('## CPM Integration')) {
        const cpmSection = `

## CPM Integration

This project uses the **Cinematic Production Module (CPM)** for AI video generation.

### CPM Commands
- \`/cpm\` - Start the Shard Generation Ritual
- \`/cpm-new-project\` - Scaffold a new cinematic project

### CPM Agents
When generating video prompts, invoke the Four-Agent Ritual:
1. **Showrunner** - Story and narrative (WHAT happens)
2. **Cinematographer** - Visual specs (HOW it looks)
3. **Script Supervisor** - Continuity validation (STATE is correct)
4. **Prompt Engineer** - Final prompt compilation

### Key Files
- \`.cpm/manifest.md\` - Context index for current scene
- \`Bible/Show_Bible.md\` - Story, themes, world rules
- \`Architecture/Style_Guide.md\` - Visual language and constraints
`;

        await fs.appendFile(claudeMdPath, cpmSection);
        logger.log(chalk.green('✓ Added CPM section to CLAUDE.md'));
      }
    }

    logger.log(chalk.green('✓ Claude Code configuration complete'));
    return true;
  } catch (error) {
    logger.warn(chalk.yellow(`Warning: Claude Code config failed: ${error.message}`));
    return false;
  }
}

module.exports = { install };
