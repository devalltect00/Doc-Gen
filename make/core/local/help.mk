# Help for Doc Gen commands executed locally.

.PHONY: help-local-init help-local-structure
help-local-init:
	@echo [Local Initialization] $(call HELP_TOTAL,LOCAL_INIT)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make l-init                         $(HELP_COLUMN_SEPARATOR)    Run initialization with custom variables
	@echo   make l-init-force                   $(HELP_COLUMN_SEPARATOR)    Overwrite existing initialization files
	@echo   make l-init-ask                     $(HELP_COLUMN_SEPARATOR)    Ask before overwriting files
	@echo   make l-init-all                     $(HELP_COLUMN_SEPARATOR)    Initialize all resources
	@echo   make l-init-config                  $(HELP_COLUMN_SEPARATOR)    Initialize configuration only
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)

help-local-structure:
	@echo [Local Structure Workflows] $(call HELP_TOTAL,LOCAL_STRUCTURE)
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
	@echo   make l-generate TARGET=.            $(HELP_COLUMN_SEPARATOR)    Generate project structure documentation
	@echo   make l-generate-smart TARGET=.      $(HELP_COLUMN_SEPARATOR)    Generate using smart mode
	@echo   make l-print TARGET=.               $(HELP_COLUMN_SEPARATOR)    Print project structure
	@echo   make l-print-smart TARGET=.         $(HELP_COLUMN_SEPARATOR)    Print using smart mode
	@echo   make l-analyze TARGET=.             $(HELP_COLUMN_SEPARATOR)    Analyze project structure
	@echo   make l-analyze-smart TARGET=.       $(HELP_COLUMN_SEPARATOR)    Analyze using smart mode
	@echo $(HELP_SEPARATOR)
	@$(ECHO_BLANK)
