0. Planning is 80% of success. Write your feature spec BEFORE opening Claude. AI amplifies clarity or confusion, your choice
1. AI can build anything with the right context. Give screenshots, file structures, database schemas, API docs, everything
2. XML formatted prompts work 3x better than plaintext. LLMs parse structured data natively
3. Stop building one mega agent. Build many specialized ones that do ONE thing perfectly
4. MCPs save 80% of context and prevent memory loss. Non-negotiable for serious work
5. At 50% token limit, start fresh. Compaction progressively degrades output quality
6. Create custom commands for repetitive tasks. Two hours saved daily, minimum
7. Claude Code hooks are criminally underused. Set once, benefit forever
8. One feature per chat, always. Mixing features is coding drunk
9. After every completion: "Review your work and list what might be broken"
10. Screenshots provide 10x more context than text. Drag directly into terminal
11. Loop tests until it actually works. "Should work" means it doesn't
12. Keep rules files under 100 lines. Concise beats comprehensive
13. Write tests BEFORE code. TDD with AI prevents debugging nightmares
14. Maintain PROJECT_CONTEXT.md updated after each session for continuity
15. For fixes: "Fix this without changing anything else" prevents cascade failures
16. Separate agents for frontend/backend/database work better than one
17. "Explain what you changed and why" forces actual understanding
18. Set checkpoints: "Stop after X and wait" prevents runaway changes
19. Git commit after EVERY working feature. Reverting beats fixing
20. Generate a debug plan before debugging. Random attempts waste tokens
21. "Write code your future self can modify" produces 10x cleaner output
22. Keep DONT_DO.md with past failures. AI forgets but you shouldn't
23. Start each session with: project context, rules, what not to do
24. If confused, the AI is too. Clarify for yourself first
25. Have pre-defined agents and rules FOR YOUR techstack. I find websites like [vibecodingtools.tech](vibecodingtools.tech) and [cursor.directory](cursor.directory) pretty useful for this
26. Give Claude Code tasks one at a time. When you chain too many steps together, mistakes pile up. Treat yourself as the orchestrator, not Claude Code. Review every line before trusting the output.
27. Use the Playwright MCP with the Sonnet model for UI work. It can check the interface, test it, read the browser console, and catch problems better than screenshots alone.
28. For long tasks, keep context. Instead of wiping the conversation, return to a saved point. I often let Claude Code create its own internal to-do list, then handle one task at a time before going back.
29. Use cheaper sub-agents for small tasks like web searches, API lookups, or documentation checks. This keeps the main agent's context clean and reduces token use.
30. Direct Claude Code clearly when using sub-agents. Say “Use X agent for Y task” instead of expecting Claude Code to route things correctly on its own.
31. Use sub-agents mainly to gather information, not to make changes. This keeps you in control of what actually gets executed.
32. Add CLAUDE.md files in specific directories with rules for those areas. Example: in your API folder, a CLAUDE.md file can block requests outside a certain IP range.
33. Before sending prompts to Claude Code, run them through another LLM for clarity. Even better: preload that LLM with your project context for more accurate instructions.
34. Build slash commands for routine jobs like debugging or code cleanup. You save time and ensure consistent instructions every time.
35. When refactoring, keep a progress log in .md or .json format. Require Claude Code to update it after every step so nothing gets lost.
41. Use Opus 4.1 for tough reasoning tasks. Use Sonnet 4 for everything else to save tokens and speed up responses.
42. Always plan with Opus 4.1 but use a different model for actual coding. Planning and execution work better when separated.
43. If you want undo features like Cursor, check out the [ccundorepo](https://github.com/RonitSachdev/ccundo) on GitHub. It adds version control for Claude Code's edits.
44. Add a rule or hook so Claude Code automatically runs security scanners like CodeRabbit after every change.
45. Claude Code doesn't write secure code by default. Explicitly ask for protections against SQL injections, XSS, and unauthorized access. For databases like Supabase, turn on RLS from the start.
46. Require Claude Code to add rate limits to your APIs using libraries like Upstash's ratelimiter to prevent abuse or DDoS attacks.
47. Typing "think," "think hard", "think harder" or "ultrathink" forces Claude Code to reason more deeply, using more tokens. Only use this for complex debugging or analysis — it won't always give better results.
48. If Claude Code ignores rules in CLAUDE.md, repeat them in the chat with “#” and save them again in your project files. Rules often vanish after conversation compaction.
49. Keep a global Claude Code configuration that stores lessons learned, rules, and past decisions. This gives all agents a single source of truth as your tools and workflows evolve.
50. Encourage agents to update this global knowledge base daily. Over time, they get better at using past experiences to avoid old mistakes.