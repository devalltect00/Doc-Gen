# Doc Gen and developer commands executed through Docker Compose.

COMPOSE_INIT_COMMANDS_LIST := c-init c-init-force c-init-ask c-init-all c-init-config
COMPOSE_STRUCTURE_COMMANDS_LIST := c-generate c-generate-smart c-print c-print-smart c-analyze c-analyze-smart
COMPOSE_UTILITIES_COMMANDS_LIST := c-test c-lint c-lint-fix c-format c-format-check c-docs c-shell c-build-package c-exec-shell c-fix c-check c-qa c-ci

$(foreach cmd,$(COMPOSE_INIT_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,COMPOSE_INIT,$(cmd),COMPOSE)))
$(foreach cmd,$(COMPOSE_STRUCTURE_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,COMPOSE_STRUCTURE,$(cmd),COMPOSE)))
$(foreach cmd,$(COMPOSE_UTILITIES_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,COMPOSE_UTILITIES,$(cmd),COMPOSE)))

.PHONY: c-init c-init-force c-init-ask c-init-all c-init-config
c-init: docker-check
	$(COMPOSE_PROD_RUN_APP) $(COMPOSE_DOC_GEN_GLOBAL_ARGS) init $(COMPOSE_DOC_GEN_INIT_ARGS) $(COMPOSE_DOC_GEN_EXTRA_ARGS)

c-init-force: override COMPOSE_DOC_GEN_INIT_ARGS += --force
c-init-force: c-init

c-init-ask: override COMPOSE_DOC_GEN_INIT_ARGS += --ask
c-init-ask: c-init

c-init-all: override COMPOSE_DOC_GEN_INIT_ARGS += --mode all
c-init-all: c-init

c-init-config: override COMPOSE_DOC_GEN_INIT_ARGS += --mode config
c-init-config: c-init

.PHONY: c-generate c-generate-smart c-print c-print-smart c-analyze c-analyze-smart
c-generate: docker-check
	$(COMPOSE_PROD_RUN_APP) $(COMPOSE_DOC_GEN_GLOBAL_ARGS) structure generate $(COMPOSE_DOC_GEN_GENERATE_ARGS) $(COMPOSE_DOC_GEN_STRUCTURE_ARGS) $(COMPOSE_DOC_GEN_EXTRA_ARGS)

c-generate-smart: override COMPOSE_DOC_GEN_GENERATE_ARGS += --smart
c-generate-smart: c-generate

c-print: docker-check
	$(COMPOSE_PROD_RUN_APP) $(COMPOSE_DOC_GEN_GLOBAL_ARGS) structure print $(COMPOSE_DOC_GEN_PRINT_ARGS) $(COMPOSE_DOC_GEN_STRUCTURE_ARGS) $(COMPOSE_DOC_GEN_EXTRA_ARGS)

c-print-smart: override COMPOSE_DOC_GEN_PRINT_ARGS += --smart
c-print-smart: c-print

c-analyze: docker-check
	$(COMPOSE_PROD_RUN_APP) $(COMPOSE_DOC_GEN_GLOBAL_ARGS) structure analyze $(COMPOSE_DOC_GEN_ANALYZE_ARGS) $(COMPOSE_DOC_GEN_STRUCTURE_ARGS) $(COMPOSE_DOC_GEN_EXTRA_ARGS)

c-analyze-smart: override COMPOSE_DOC_GEN_ANALYZE_ARGS += --smart
c-analyze-smart: c-analyze

.PHONY: c-test c-lint c-lint-fix c-format c-format-check c-docs c-shell c-build-package c-exec-shell
c-test: c-build-dev
	$(COMPOSE_DEV_RUN_TEST)
c-lint: c-build-dev
	$(COMPOSE_DEV_RUN_LINT)
c-lint-fix: c-build-dev
	$(COMPOSE_DEV_RUN_LINT_FIX)
c-format: c-build-dev
	$(COMPOSE_DEV_RUN_FORMAT)
c-format-check: c-build-dev
	$(COMPOSE_DEV_RUN_FORMAT_CHECK)
c-docs: docker-check
	$(COMPOSE_DEV_UP_DOCS) -d
c-shell: c-build-dev
	$(COMPOSE_DEV_RUN_SHELL)
c-build-package: c-build-dev
	$(COMPOSE_DEV_RUN_BUILD)
c-exec-shell: docker-check
	$(COMPOSE_DEV_EXEC) $(SERVICE_APP) $(SHELL_BIN)

.PHONY: c-fix c-check c-qa c-ci
c-fix: docker-check
	@$(MAKE) --no-print-directory c-format
	@$(MAKE) --no-print-directory c-lint-fix
c-check: docker-check
	@$(MAKE) --no-print-directory c-format-check
	@$(MAKE) --no-print-directory c-lint
	@$(MAKE) --no-print-directory c-test
c-qa: docker-check
	@$(MAKE) --no-print-directory c-fix
	@$(MAKE) --no-print-directory c-check
c-ci: docker-check
	@$(MAKE) --no-print-directory c-build-dev
	@$(MAKE) --no-print-directory c-check
