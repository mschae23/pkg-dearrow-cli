FEDORA_RELEASE=42
FEDORA_ARCH=x86_64

FEDPKG=fedpkg
RPM=rpm
CURL=curl

build-all:
.PHONY: build-all

FEDPKG_FLAGS=
MOCKBUILD_FLAGS=

FORGEJO_PACKAGE_USER=mschae23
FORGEJO_USERNAME=$(FORGEJO_PACKAGE_USER)
# FORGEJO_PUBLISH_FLAG=--upload-file #
FORGEJO_PUBLISH_FLAG=-X PUT -F upload=@
FORGEJO_PUBLISH={ echo -n 'user = "$(FORGEJO_USERNAME):'; cat $(FORGEJO_PASSWORD_FILE); echo '"'; } | $(CURL) -K - -w '\n' $(FORGEJO_PUBLISH_FLAG)
FORGEJO_API_ROOT=https://code.mschae23.de
FORGEJO_UPLOAD_PATH=$(FORGEJO_API_ROOT)/api/packages/$(FORGEJO_PACKAGE_USER)/rpm/fc$(FEDORA_RELEASE)/upload
FORGEJO_SOURCE_UPLOAD_PATH=$(FORGEJO_API_ROOT)/api/packages/$(FORGEJO_PACKAGE_USER)/rpm/fc$(FEDORA_RELEASE)-source/upload

define PACKAGES
$(eval $(call package_template,mschae23-repos,mschae23-repos,mschae23-repos,$(FEDORA_RELEASE),2,noarch))\
$(eval $(call package_template,rust-dearrow-browser,rust-dearrow-browser,rust-dearrow-browser-api-devel,1.14.0,2,noarch))\
$(eval $(call package_template,rust-tabled_derive,rust-tabled_derive,rust-tabled_derive-devel,0.11.0,1,noarch))\
$(eval $(call package_template,rust-testing_table,rust-testing_table,rust-testing_table-devel,0.3.0,1,noarch))\
$(eval $(call package_template,rust-papergrid,rust-papergrid,rust-papergrid-devel,0.15.0,1,noarch))\
$(eval $(call package_template,rust-tabled,rust-tabled,rust-tabled-devel,0.19.0,1,noarch))\
$(eval $(call package_template,dearrow-cli,dearrow-cli,dearrow-cli,4.3.0,3,$(FEDORA_ARCH)))
endef

define PUBLISH_TARGETS
$(call publish_template,dearrow-cli)

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

publish-rust-tabled: build-rust-tabled
	$(FORGEJO_PUBLISH)$(rust-tabled_rpm_target_dir)/rust-tabled-devel-$(rust-tabled_package_version)-$(rust-tabled_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-tabled_rpm_target_dir)/rust-tabled+default-devel-$(rust-tabled_package_version)-$(rust-tabled_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-tabled_rpm_target_dir)/rust-tabled+std-devel-$(rust-tabled_package_version)-$(rust-tabled_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-tabled_rpm_target_dir)/rust-tabled+derive-devel-$(rust-tabled_package_version)-$(rust-tabled_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-tabled_rpm_target_dir)/rust-tabled+ansi-devel-$(rust-tabled_package_version)-$(rust-tabled_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-tabled_rpm_target_dir)/rust-tabled+ansi-str-devel-$(rust-tabled_package_version)-$(rust-tabled_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-tabled_rpm_target_dir)/rust-tabled+ansitok-devel-$(rust-tabled_package_version)-$(rust-tabled_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-tabled_rpm_target_dir)/rust-tabled+macros-devel-$(rust-tabled_package_version)-$(rust-tabled_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-tabled_rpm_target_dir)/rust-tabled+assert-devel-$(rust-tabled_package_version)-$(rust-tabled_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-tabled_rpm_target_dir)/rust-tabled+tabled_derive-devel-$(rust-tabled_package_version)-$(rust-tabled_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-tabled_rpm_target_dir)/rust-tabled+testing_table-devel-$(rust-tabled_package_version)-$(rust-tabled_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
.PHONY: publish-rust-tabled

publish-rust-papergrid: build-rust-papergrid
	$(FORGEJO_PUBLISH)$(rust-papergrid_rpm_target_dir)/rust-papergrid-devel-$(rust-papergrid_package_version)-$(rust-papergrid_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-papergrid_rpm_target_dir)/rust-papergrid+default-devel-$(rust-papergrid_package_version)-$(rust-papergrid_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-papergrid_rpm_target_dir)/rust-papergrid+std-devel-$(rust-papergrid_package_version)-$(rust-papergrid_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-papergrid_rpm_target_dir)/rust-papergrid+ansi-devel-$(rust-papergrid_package_version)-$(rust-papergrid_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-papergrid_rpm_target_dir)/rust-papergrid+ansi-str-devel-$(rust-papergrid_package_version)-$(rust-papergrid_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-papergrid_rpm_target_dir)/rust-papergrid+ansitok-devel-$(rust-papergrid_package_version)-$(rust-papergrid_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-papergrid_rpm_target_dir)/rust-papergrid+ahash-devel-$(rust-papergrid_package_version)-$(rust-papergrid_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
.PHONY: publish-rust-papergrid

publish-rust-testing_table: build-rust-testing_table
	$(FORGEJO_PUBLISH)$(rust-testing_table_rpm_target_dir)/rust-testing_table-devel-$(rust-testing_table_package_version)-$(rust-testing_table_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-testing_table_rpm_target_dir)/rust-testing_table+default-devel-$(rust-testing_table_package_version)-$(rust-testing_table_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-testing_table_rpm_target_dir)/rust-testing_table+ansi-devel-$(rust-testing_table_package_version)-$(rust-testing_table_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-testing_table_rpm_target_dir)/rust-testing_table+ansitok-devel-$(rust-testing_table_package_version)-$(rust-testing_table_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-testing_table_rpm_target_dir)/rust-testing_table+std-devel-$(rust-testing_table_package_version)-$(rust-testing_table_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
.PHONY: publish-rust-testing_table

publish-rust-tabled_derive: build-rust-tabled_derive
	$(FORGEJO_PUBLISH)$(rust-tabled_derive_rpm_target) $(FORGEJO_UPLOAD_PATH)
	$(FORGEJO_PUBLISH)$(rust-tabled_derive_rpm_target_dir)/rust-tabled_derive+default-devel-$(rust-tabled_derive_package_version)-$(rust-tabled_derive_package_release).fc$(FEDORA_RELEASE).noarch.rpm $(FORGEJO_UPLOAD_PATH)
.PHONY: publish-rust-tabled_derive

publish-mschae23-repos: build-mschae23-repos
	$(FORGEJO_PUBLISH)$(mschae23-repos_rpm_target) $(FORGEJO_UPLOAD_PATH)
.PHONY: publish-mschae23-repos
endef

## Everything below is generic

rpm_target_dir = $1/results_$$($1_package_name)/$$($1_package_version)/$$($1_package_release).fc$(FEDORA_RELEASE)
rpm_target = $(call rpm_target_dir,$1)/$$($1_built_package_name)-$$($1_package_version)-$$($1_package_release).fc$(FEDORA_RELEASE).$$($1_package_arch).rpm

define package_template
$1_spec_dir := $1
$1_package_name := $2
$1_built_package_name := $3
$1_package_version := $4
$1_package_release := $5
$1_package_arch := $6
$1_rpm_target_dir := $(call rpm_target_dir,$$($1_spec_dir))
$1_rpm_target := $(call rpm_target,$$($1_spec_dir))

$$($1_rpm_target): $$($1_spec_dir)/$$($1_package_name).spec
	$(FEDPKG) $(FEDPKG_FLAGS) --path ./$$($1_spec_dir)/ --release f$(FEDORA_RELEASE) mockbuild $(MOCKBUILD_FLAGS)
	shopt -s nullglob; $(RPM) --addsign $$($1_rpm_target_dir)/*-$$($1_package_version)-$$($1_package_release).fc$(FEDORA_RELEASE).*.rpm

$$($1_spec_dir)/$$($1_package_name).spec: $(wildcard $$($1_spec_dir)/*.patch)

build-$$($1_spec_dir): $$($1_rpm_target)
.PHONY: build-$$($1_spec_dir)

build-all: build-$$($1_spec_dir)
endef

define publish_template
publish-$$($1_spec_dir): $$($1_rpm_target)
	$(FORGEJO_PUBLISH)$($1_rpm_target) $(FORGEJO_UPLOAD_PATH)
.PHONY: publish-$$($1_spec_dir)
endef

$(eval $(PACKAGES))
$(eval $(PUBLISH_TARGETS))
