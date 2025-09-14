Name:           mschae23-repos
Version:        42
Release:        2%{?dist}
Summary:        mschae23 package repositories

License:        MIT
URL:            https://code.mschae23.de/mschae23/pkg-dearrow-cli
Source0:        mschae23.repo
BuildArch:      noarch

Requires:       system-release(%{version})

%description
Release package containing mschae23's repository configuration.

%prep

%build

%install
install -D -p -m 0644 -t %{buildroot}%{_sysconfdir}/yum.repos.d %{SOURCE0}

%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/mschae23.repo

%changelog
* Sun Sep 14 2025 mschae23 <pkg@mschae23.de> - 42-2
- Update repository URLs

* Sun May 04 2025 mschae23 <pkg@mschae23.de> - 42-1
- Rebuild for Fedora 42

* Sun May 04 2025 mschae23 <pkg@mschae23.de> - 41-2
- Update Forgejo links

* Mon Nov 25 2024 mschae23 <pkg@mschae23.de> - 41-1
- Initial package

