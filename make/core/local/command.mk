# Doc Gen commands executed from the project virtual environment.

LOCAL_INIT_COMMANDS_LIST := l-init l-init-force l-init-ask l-init-all l-init-config
LOCAL_STRUCTURE_COMMANDS_LIST := l-generate l-generate-smart l-print l-print-smart l-analyze l-analyze-smart

$(foreach cmd,$(LOCAL_INIT_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,LOCAL_INIT,$(cmd),LOCAL)))
$(foreach cmd,$(LOCAL_STRUCTURE_COMMANDS_LIST),$(eval $(call REGISTER_COMMAND,LOCAL_STRUCTURE,$(cmd),LOCAL)))

.PHONY: l-init l-init-force l-init-ask l-init-all l-init-config
l-init: check-venv
	$(LOCAL_RUN) $(LOCAL_DOC_GEN_GLOBAL_ARGS) init $(LOCAL_DOC_GEN_INIT_ARGS) $(LOCAL_DOC_GEN_EXTRA_ARGS)

l-init-force: override LOCAL_DOC_GEN_INIT_ARGS += --force
l-init-force: l-init

l-init-ask: override LOCAL_DOC_GEN_INIT_ARGS += --ask
l-init-ask: l-init

l-init-all: override LOCAL_DOC_GEN_INIT_ARGS += --mode all
l-init-all: l-init

l-init-config: override LOCAL_DOC_GEN_INIT_ARGS += --mode config
l-init-config: l-init

.PHONY: l-generate l-generate-smart l-print l-print-smart l-analyze l-analyze-smart
l-generate: check-venv
	$(LOCAL_RUN) $(LOCAL_DOC_GEN_GLOBAL_ARGS) structure generate $(LOCAL_DOC_GEN_GENERATE_ARGS) $(LOCAL_DOC_GEN_STRUCTURE_ARGS) $(LOCAL_DOC_GEN_EXTRA_ARGS)

l-generate-smart: override LOCAL_DOC_GEN_GENERATE_ARGS += --smart
l-generate-smart: l-generate

l-print: check-venv
	$(LOCAL_RUN) $(LOCAL_DOC_GEN_GLOBAL_ARGS) structure print $(LOCAL_DOC_GEN_PRINT_ARGS) $(LOCAL_DOC_GEN_STRUCTURE_ARGS) $(LOCAL_DOC_GEN_EXTRA_ARGS)

l-print-smart: override LOCAL_DOC_GEN_PRINT_ARGS += --smart
l-print-smart: l-print

l-analyze: check-venv
	$(LOCAL_RUN) $(LOCAL_DOC_GEN_GLOBAL_ARGS) structure analyze $(LOCAL_DOC_GEN_ANALYZE_ARGS) $(LOCAL_DOC_GEN_STRUCTURE_ARGS) $(LOCAL_DOC_GEN_EXTRA_ARGS)

l-analyze-smart: override LOCAL_DOC_GEN_ANALYZE_ARGS += --smart
l-analyze-smart: l-analyze
