Name:           confd
Version:        0.17.109
Release:        1%{?git_date:.%{git_date}}%{?git_hash:git%{git_hash}}
Summary:        Manage local application configuration files using templates and data from etcd or consul

Group:          System Environment/Daemons
License:        MPLv2.0
URL:            http://www.confd.io
%ifarch x86_64
%define confd_arch amd64
%endif
%ifarch aarch64
%define confd_arch arm64
%endif
%if "%{confd_arch}" == "%%{confd_arch}"
%{error:unsupported architecture}
%endif
%undefine _disable_source_fetch
Source0:        https://github.com/seewerah/confd/releases/download/v%{version}/confd-%{version}-linux-%{confd_arch}

%description
Manage local application configuration files using templates and data from etcd or consul

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 0755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}
mkdir -p \
    %{buildroot}/%{_sysconfdir}/%{name}/conf.d \
    %{buildroot}/%{_sysconfdir}/%{name}/templates

%files
%defattr(-,root,root,-)
%{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/conf.d
%{_sysconfdir}/%{name}/templates
%{_bindir}/confd

%doc

%changelog
* Thu Sep 19 2024 Fernando Silveira <fsilveira@gmail.com>
- Removed init scripts
- Bumped version to 0.17.109
- Added support for amd64
* Fri Dec 6 2018 Jean-Sébastien Frerot <jean-sebastien@frerot.me>
- Create and use conf.d by default in /etc/confd
- Add templates folder in /etc/confd/
* Thu Dec 5 2018 Jean-Sébastien Frerot <jean-sebastien@frerot.me>
- Fix Non working part of the spec file
* Fri Jan 16 2015 Michael Chapman <michchcap@cisco.com>
- Initial
