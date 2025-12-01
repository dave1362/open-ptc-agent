# Changelog

All notable changes to Open PTC Agent are documented here.

Repository: https://github.com/Chen-zexi/open-ptc-agent

## [Nov 27 - Dec 1, 2025]

### Added
- Background subagent execution with waiting room pattern, allowing the main agent to continue working while subagents run asynchronously ([46fcf49](https://github.com/Chen-zexi/open-ptc-agent/commit/46fcf49))
- ViewImageMiddleware for multimodal image input support during agent runtime ([f62a4e6](https://github.com/Chen-zexi/open-ptc-agent/commit/f62a4e6))
- Configurable subagents section in config.yaml with `general-purpose` and `research` agents ([ee7cef1](https://github.com/Chen-zexi/open-ptc-agent/commit/ee7cef1))
- `wait()` and `check_task_progress()` tools for monitoring background tasks ([46fcf49](https://github.com/Chen-zexi/open-ptc-agent/commit/46fcf49))
- Gemini-3-pro-image model configuration in llms.json ([a95ec60](https://github.com/Chen-zexi/open-ptc-agent/commit/a95ec60))

### Changed
- Reorganized prompt templates with new subagent coordination, tool discovery, and data processing components ([895b01b](https://github.com/Chen-zexi/open-ptc-agent/commit/895b01b))
- Extracted config factory functions to `config_loader.py` for DRY configuration loading ([ee7cef1](https://github.com/Chen-zexi/open-ptc-agent/commit/ee7cef1))
- Improved sandbox string formatting using `textwrap.dedent` for cleaner multi-line code ([a95ec60](https://github.com/Chen-zexi/open-ptc-agent/commit/a95ec60))

### Fixed
- Grep result parsing now handles string format `path:line:text` in addition to dict format ([a95ec60](https://github.com/Chen-zexi/open-ptc-agent/commit/a95ec60))
- Glob pattern matching no longer adds `**/` prefix to patterns containing paths ([a95ec60](https://github.com/Chen-zexi/open-ptc-agent/commit/a95ec60))
- Hardcoded test paths replaced with dynamic paths ([6448ec3](https://github.com/Chen-zexi/open-ptc-agent/commit/6448ec3))

## [~ - Nov 27 2025]
- Initial release of Open PTC Agent ([14e1d8f](https://github.com/Chen-zexi/open-ptc-agent/commit/14e1d8f))