# Help text for commonly overridden Make variables.

.PHONY: help-variables
help-variables:
	@echo [Common Variables]
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   DOC_GEN_GLOBAL_ARGS="args"          $(HELP_COLUMN_SEPARATOR)    Global Doc Gen options
	@echo   DOC_GEN_INIT_ARGS="args"            $(HELP_COLUMN_SEPARATOR)    Options passed to init
	@echo   DOC_GEN_STRUCTURE_ARGS="args"       $(HELP_COLUMN_SEPARATOR)    Shared target and structure options
	@echo   DOC_GEN_GENERATE_ARGS="args"        $(HELP_COLUMN_SEPARATOR)    Options passed to structure generate
	@echo   DOC_GEN_PRINT_ARGS="args"           $(HELP_COLUMN_SEPARATOR)    Options passed to structure print
	@echo   DOC_GEN_ANALYZE_ARGS="args"         $(HELP_COLUMN_SEPARATOR)    Options passed to structure analyze
	@echo   TARGET=path                         $(HELP_COLUMN_SEPARATOR)    Repository target, default: .
	@$(ECHO_BLANK)
	@echo   VENV_NAME=name                      $(HELP_COLUMN_SEPARATOR)    Virtual environment directory, default: venv
	@echo   DOCKER_TAG=tag                      $(HELP_COLUMN_SEPARATOR)    Local Docker image tag, default: latest
	@echo   DOCKER_TTY=                         $(HELP_COLUMN_SEPARATOR)    Disable interactive Docker flags for automation
	@echo   DOCKER_WORKSPACE_HOST=path          $(HELP_COLUMN_SEPARATOR)    Host workspace mounted by direct Docker commands
	@echo   CUSTY_CREDENTIALS_MOUNT=true/false  $(HELP_COLUMN_SEPARATOR)    Opt in to the read-only Custy credential mount
	@echo   CUSTY_CREDENTIALS_HOST_DIR=path     $(HELP_COLUMN_SEPARATOR)    External host credential directory
	@echo   CUSTY_CREDENTIALS_CONTAINER_DIR=path $(HELP_COLUMN_SEPARATOR)   Container credential directory
	@echo   CUSTY_CREDENTIALS_REMOTE=name       $(HELP_COLUMN_SEPARATOR)    Remote tested by credential helper targets
	@$(ECHO_BLANK)
	@echo   GHCR_REGISTRY=host                  $(HELP_COLUMN_SEPARATOR)    Published container registry host
	@echo   GHCR_OWNER=owner                    $(HELP_COLUMN_SEPARATOR)    Published container registry owner
	@echo   REMOTE_TAG=tag                      $(HELP_COLUMN_SEPARATOR)    Published image tag, default: latest
	@echo   REMOTE_WORKSPACE=path               $(HELP_COLUMN_SEPARATOR)    Host workspace mounted into a remote container
	@echo   REMOTE_IMAGE_PHS=name               $(HELP_COLUMN_SEPARATOR)    Path Header Scanner image repository
	@echo   REMOTE_IMAGE_DOC_GEN=name           $(HELP_COLUMN_SEPARATOR)    Doc Gen image repository
	@echo   REMOTE_IMAGE_CUSTY=name             $(HELP_COLUMN_SEPARATOR)    Custy image repository
	@echo   REMOTE_IMAGE_REFLOW=name            $(HELP_COLUMN_SEPARATOR)    Reflow image repository
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
