VERSION := $(shell git describe --tags | sed 's/v//')

.PHONY: default
default:
	@echo "WTF, MATE?"

.PHONY: test
test:
	@python3 fox_hex_utils_test.py && echo "Everything seems to check out, boss!"

.PHONY: release
release:
	@rm -rf build
	@mkdir -p build/
	@cp license hex-utils-license
	@zip -r build/hex-utils-$(VERSION).zip \
		hex-utils-license \
		fox_hex_utils_ren.py \
		fox_requirement_ren.py
	@rm hex-utils-license