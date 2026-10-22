# Risk Decoded — episode pipeline (Phase 0 stubs)
# Real stage logic lands in src/orchestrator during Phase 3.
# Usage: make episode EP=ep01

EP ?= ep01
CONFIG = config/episodes/$(EP).yaml
BUILD  = build/$(EP)

.PHONY: help validate voice stills render shorts package episode clean

help:
	@echo "Targets: validate | voice | stills | render | shorts | package | episode (all) | clean"
	@echo "Usage:   make episode EP=ep01"

$(BUILD):
	mkdir -p $(BUILD)

validate: $(BUILD)
	@echo "[validate] TODO: parse scripts/$(EP)-*.md -> $(BUILD)/scenes.json; validate vs config/scene.schema.json"

voice: validate
	@echo "[voice] TODO: ElevenLabs synth from scenes -> $(BUILD)/narration.mp3 + timings.json (voice_id from $(CONFIG))"

stills: validate
	@echo "[stills] TODO: Nano Banana scene art + thumbnail -> assets/generated/$(EP)/ (respect image.max_images cap)"

render: voice stills
	@echo "[render] TODO: Remotion compose Qubit + panels + captions -> $(BUILD)/$(EP).mp4"

shorts: render
	@echo "[shorts] TODO: cut vertical Shorts from long-form -> $(BUILD)/shorts/*.mp4"

package: shorts
	@echo "[package] TODO: assemble upload package (video, title, description, tags, thumbnail, review packet) -> $(BUILD)/package/. Never uploads."

episode: package
	@echo "[episode] $(EP) complete -> $(BUILD)/ (review packet + upload package)"

clean:
	rm -rf $(BUILD)
