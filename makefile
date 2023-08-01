VERSION := $(shell git describe --tags | sed 's/v//')

.PHONY: default
default:
	@echo "WTF, MATE?"

.PHONY: test
test:
	@python3 fox_hex_utils_ren.py && echo "Everything seems to check out, boss!"

.PHONY: release
release:
	@rm -rf .build
	@mkdir -p .build/
	@zip .build/hex-utils-$(VERSION).zip license fox_hex_utils_ren.py requirement_ren.py