FEDORA_RELEASE=41
FEDORA_ARCH=x86_64

FEDPKG=fedpkg
RPM=rpm
CURL=curl

build-all: build-mschae23-repos build-rust-dearrow-browser build-dearrow-cli
.PHONY: build-all

FORGEJO_PACKAGE_USER=mschae23
FORGEJO_USERNAME=$(FORGEJO_PACKAGE_USER)
FORGEJO_PUBLISH_FLAG=--upload-file #
FORGEJO_PUBLISH={ echo -n 'user = "$(FORGEJO_USERNAME):'; cat $(FORGEJO_PASSWORD_FILE); echo '"'; } | $(CURL) -K - -w '\n' $(FORGEJO_PUBLISH_FLAG)
FORGEJO_API_ROOT=https://code.mschae23.de
FORGEJO_UPLOAD_PATH=$(FORGEJO_API_ROOT)/api/packages/$(FORGEJO_PACKAGE_USER)/rpm/fc$(FEDORA_RELEASE)/upload

define PACKAGES
$(eval $(call package_template,mschae23-repos,mschae23-repos,mschae23-repos,41,2,noarch)) \
$(eval $(call package_template,rust-dearrow-browser,rust-dearrow-browser,rust-dearrow-browser,1.14.0,2,src)) \
$(eval $(call package_template,dearrow-cli,dearrow-cli,dearrow-cli,4.3.0,2,$(FEDORA_ARCH)))
endef

publish-dearrow-cli: build-dearrow-cli
	$(FORGEJO_PUBLISH)$(dearrow-cli_rpm_target) $(FORGEJO_UPLOAD_PATH)
.PHONY: publish-dearrow-cli

publish-rust-dearrow-browser: build-rust-dearrow-browser
	$(FORGEJO_PUBLISH)$(rust-dearrow-browser_rpm_target_dir)/rust-dearrow-browser-api-devel-$(rust-dearrow-browser_package_version)-$(rust-dearrow-browser_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-dearrow-browser_rpm_target_dir)/rust-dearrow-browser-api+default-devel-$(rust-dearrow-browser_package_version)-$(rust-dearrow-browser_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-dearrow-browser_rpm_target_dir)/rust-dearrow-browser-api+sync-devel-$(rust-dearrow-browser_package_version)-$(rust-dearrow-browser_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-dearrow-browser_rpm_target_dir)/rust-dearrow-browser-api+unsync-devel-$(rust-dearrow-browser_package_version)-$(rust-dearrow-browser_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-dearrow-browser_rpm_target_dir)/rust-dearrow-browser-api+boxed-devel-$(rust-dearrow-browser_package_version)-$(rust-dearrow-browser_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-dearrow-browser_rpm_target_dir)/rust-dearrow-browser-api+string-devel-$(rust-dearrow-browser_package_version)-$(rust-dearrow-browser_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-dearrow-browser_rpm_target_dir)/rust-dearrow-parser-devel-$(rust-dearrow-browser_package_version)-$(rust-dearrow-browser_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-dearrow-browser_rpm_target_dir)/rust-dearrow-parser+default-devel-$(rust-dearrow-browser_package_version)-$(rust-dearrow-browser_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-dearrow-browser_rpm_target_dir)/rust-error-handling-devel-$(rust-dearrow-browser_package_version)-$(rust-dearrow-browser_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-dearrow-browser_rpm_target_dir)/rust-error-handling+default-devel-$(rust-dearrow-browser_package_version)-$(rust-dearrow-browser_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
.PHONY: publish-rust-dearrow-browser

publish-mschae23-repos: build-mschae23-repos
	$(FORGEJO_PUBLISH)$(mschae23-repos_rpm_target) $(FORGEJO_UPLOAD_PATH)
.PHONY: publish-mschae23-repos

## Everything below is generic

define rpm_target_dir
$(let spec_dir spec_name package_version package_release,$(1) $(2) $(3) $(4),$\
$(spec_dir)/results_$(spec_name)/$(package_version)/$(package_release).fc$(FEDORA_RELEASE))
endef

define rpm_target
$(let spec_dir spec_name package_name package_version package_release package_arch,$(1) $(2) $(3) $(4) $(5) $(6),$\
$(call rpm_target_dir,$(spec_dir),$(spec_name),$(package_version),$(package_release))/$(package_name)-$(package_version)-$(package_release).fc$(FEDORA_RELEASE).$(package_arch).rpm)
endef

define package_template
$(1)_spec_dir := $(1)
$(1)_spec_name := $(2)
$(1)_package_name := $(3)
$(1)_package_version := $(4)
$(1)_package_release := $(5)
$(1)_package_arch := $(6)
$(1)_rpm_target_dir := $$(call rpm_target_dir,$$($(1)_spec_dir),$$($(1)_spec_name),$$($(1)_package_version),$$($(1)_package_release))
$(1)_rpm_target := $$(call rpm_target,$$($(1)_spec_dir),$$($(1)_spec_name),$$($(1)_package_name),$$($(1)_package_version),$$($(1)_package_release),$$($(1)_package_arch))

$$($(1)_rpm_target): $$($(1)_spec_dir)/$$($(1)_spec_name).spec
	$(FEDPKG) --path ./$$($(1)_spec_dir)/ --release f$(FEDORA_RELEASE) mockbuild
	shopt -s nullglob; $(RPM) --addsign $$($(1)_spec_dir)/results_$$($(1)_spec_name)/$$($(1)_package_version)/$$($(1)_package_release).fc$(FEDORA_RELEASE)/*-$$($(1)_package_version)-$$($(1)_package_release).fc$(FEDORA_RELEASE).*.rpm

$$($(1)_spec_dir)/$$($(1)_spec_name).spec: $(wildcard $$($(1)_spec_dir)/*.patch)

build-$$($(1)_spec_name): $$($(1)_rpm_target)
.PHONY: build-$$($(1)_spec_name)
endef

$(foreach package,$(PACKAGES),$(package))
