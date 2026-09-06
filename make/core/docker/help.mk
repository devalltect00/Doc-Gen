# Help for Doc Gen Docker commands.

.PHONY: help-docker-build help-docker-testing help-docker-init help-docker-structure
help-docker-build:
	@echo [Docker Image Builds] $(call HELP_TOTAL,DOCKER_INFRASTRUCTURE)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make d-build-base                   $(HELP_COLUMN_SEPARATOR)    Build the base image
	@echo   make d-build-dev                    $(HELP_COLUMN_SEPARATOR)    Build the development image
	@echo   make d-build-prod                   $(HELP_COLUMN_SEPARATOR)    Build the production image
	@echo   make d-build-all                    $(HELP_COLUMN_SEPARATOR)    Build all Doc Gen images
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)

help-docker-testing:
	@echo [Docker Testing] $(call HELP_TOTAL,DOCKER_TESTING)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make d-test                         $(HELP_COLUMN_SEPARATOR)    Run tests in the development image
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)

help-docker-init:
	@echo [Docker Initialization] $(call HELP_TOTAL,DOCKER_INIT)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make d-init                         $(HELP_COLUMN_SEPARATOR)    Run initialization in the production image
	@echo   make d-init-force                   $(HELP_COLUMN_SEPARATOR)    Overwrite initialization files
	@echo   make d-init-ask                     $(HELP_COLUMN_SEPARATOR)    Ask before overwriting files
	@echo   make d-init-all                     $(HELP_COLUMN_SEPARATOR)    Initialize all resources
	@echo   make d-init-config                  $(HELP_COLUMN_SEPARATOR)    Initialize configuration only
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)

help-docker-structure:
	@echo [Docker Structure Workflows] $(call HELP_TOTAL,DOCKER_STRUCTURE)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make d-generate TARGET=.            $(HELP_COLUMN_SEPARATOR)    Generate project documentation
	@echo   make d-generate-smart TARGET=.      $(HELP_COLUMN_SEPARATOR)    Generate using smart mode
	@echo   make d-print TARGET=.               $(HELP_COLUMN_SEPARATOR)    Print project structure
	@echo   make d-print-smart TARGET=.         $(HELP_COLUMN_SEPARATOR)    Print using smart mode
	@echo   make d-analyze TARGET=.             $(HELP_COLUMN_SEPARATOR)    Analyze project structure
	@echo   make d-analyze-smart TARGET=.       $(HELP_COLUMN_SEPARATOR)    Analyze using smart mode
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
