# Practical examples for Doc Gen Make workflows.

.PHONY: help-examples
help-examples:
	@echo [Examples]
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo [Local Doc Gen Workflow]
	@echo   make setup
	@echo   make l-generate-smart TARGET=.
	@echo   make l-print TARGET=.
	@echo   make l-analyze TARGET=.
	@$(ECHO_BLANK)
	@echo [Docker and Compose Workflow]
	@echo   make d-build-all
	@echo   make c-check
	@$(ECHO_BLANK)
	@echo [Published Image Registry Workflow]
	@echo   make r-phs-pull REMOTE_TAG=latest
	@echo   make r-doc-gen-pull REMOTE_TAG=latest
	@echo   make r-custy-pull REMOTE_TAG=latest
	@echo   make r-reflow-pull REMOTE_TAG=latest
	@$(ECHO_BLANK)
	@echo [Published Utility Runtime Workflow]
	@echo   make r-phs-scan TARGET=app REMOTE_WORKSPACE="D:/project/target"
	@echo   make r-doc-generate-smart REMOTE_WORKSPACE="D:/project/target"
	@echo   make r-custy-run-validate REMOTE_WORKSPACE="D:/project/target"
	@echo   make r-reflow-tags-convert-dryrun REMOTE_WORKSPACE="D:/project/target"
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
