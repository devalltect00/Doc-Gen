# Doc Gen and test commands executed in local Docker images.

DOCKER_TESTING_COMMANDS_LIST := d-test
DOCKER_INIT_COMMANDS_LIST := d-init d-init-force d-init-ask d-init-all d-init-config
DOCKER_STRUCTURE_COMMANDS_LIST := d-generate d-generate-smart d-print d-print-smart d-analyze d-analyze-smart

$(foreach cmd,$(DOCKER_TESTING_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,DOCKER_TESTING,$(cmd),DOCKER)))
$(foreach cmd,$(DOCKER_INIT_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,DOCKER_INIT,$(cmd),DOCKER)))
$(foreach cmd,$(DOCKER_STRUCTURE_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,DOCKER_STRUCTURE,$(cmd),DOCKER)))

.PHONY: d-test
d-test: d-build-dev
	$(DOCKER_RUN_NO_ENTRYPOINT) $(DOCKER_WORKSPACE) $(DOCKER_IMAGE_DEV) python -m pytest -v

.PHONY: d-init d-init-force d-init-ask d-init-all d-init-config
d-init: docker-check
	$(DOCKER_RUN_INTERACTIVE) $(DOCKER_WORKSPACE) $(DOCKER_IMAGE_PROD) $(DOCKER_DOC_GEN_GLOBAL_ARGS) init $(DOCKER_DOC_GEN_INIT_ARGS) $(DOCKER_DOC_GEN_EXTRA_ARGS)

d-init-force: override DOCKER_DOC_GEN_INIT_ARGS += --force
d-init-force: d-init

d-init-ask: override DOCKER_DOC_GEN_INIT_ARGS += --ask
d-init-ask: d-init

d-init-all: override DOCKER_DOC_GEN_INIT_ARGS += --mode all
d-init-all: d-init

d-init-config: override DOCKER_DOC_GEN_INIT_ARGS += --mode config
d-init-config: d-init

.PHONY: d-generate d-generate-smart d-print d-print-smart d-analyze d-analyze-smart
d-generate: docker-check
	$(DOCKER_RUN_INTERACTIVE) $(DOCKER_WORKSPACE) $(DOCKER_IMAGE_PROD) $(DOCKER_DOC_GEN_GLOBAL_ARGS) structure generate $(DOCKER_DOC_GEN_GENERATE_ARGS) $(DOCKER_DOC_GEN_STRUCTURE_ARGS) $(DOCKER_DOC_GEN_EXTRA_ARGS)

d-generate-smart: override DOCKER_DOC_GEN_GENERATE_ARGS += --smart
d-generate-smart: d-generate

d-print: docker-check
	$(DOCKER_RUN_INTERACTIVE) $(DOCKER_WORKSPACE) $(DOCKER_IMAGE_PROD) $(DOCKER_DOC_GEN_GLOBAL_ARGS) structure print $(DOCKER_DOC_GEN_PRINT_ARGS) $(DOCKER_DOC_GEN_STRUCTURE_ARGS) $(DOCKER_DOC_GEN_EXTRA_ARGS)

d-print-smart: override DOCKER_DOC_GEN_PRINT_ARGS += --smart
d-print-smart: d-print

d-analyze: docker-check
	$(DOCKER_RUN_INTERACTIVE) $(DOCKER_WORKSPACE) $(DOCKER_IMAGE_PROD) $(DOCKER_DOC_GEN_GLOBAL_ARGS) structure analyze $(DOCKER_DOC_GEN_ANALYZE_ARGS) $(DOCKER_DOC_GEN_STRUCTURE_ARGS) $(DOCKER_DOC_GEN_EXTRA_ARGS)

d-analyze-smart: override DOCKER_DOC_GEN_ANALYZE_ARGS += --smart
d-analyze-smart: d-analyze
