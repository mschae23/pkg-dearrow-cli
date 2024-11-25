Name:           mschae23-repos
Version:        41
Release:        1%{?dist}
Summary:        mschae23 package repositories

License:        MIT
URL:            https://mschae23.de/git/mschae23/pkg-dearrow-cli
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
* Mon Nov 25 2024 mschae23 <pkg@mschae23.de> - 41-1
- Initial package

