%global debug_package %{nil}

Name: python-rstcheck
Epoch: 100
Version: 3.3.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Python module to check syntax of reStructuredText
License: MIT
URL: https://github.com/myint/rstcheck/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Checks syntax of reStructuredText and code blocks nested within it.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-rstcheck
Summary: Python module to check syntax of reStructuredText
Requires: python3
Requires: python3-docutils >= 0.7
Provides: python3-rstcheck = %{epoch}:%{version}-%{release}
Provides: python3dist(rstcheck) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-rstcheck = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(rstcheck) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-rstcheck = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(rstcheck) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-rstcheck
Checks syntax of reStructuredText and code blocks nested within it.

%files -n python%{python3_version_nodots}-rstcheck
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-rstcheck
Summary: Python module to check syntax of reStructuredText
Requires: python3
Requires: python3-docutils >= 0.7
Provides: python3-rstcheck = %{epoch}:%{version}-%{release}
Provides: python3dist(rstcheck) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-rstcheck = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(rstcheck) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-rstcheck = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(rstcheck) = %{epoch}:%{version}-%{release}

%description -n python3-rstcheck
Checks syntax of reStructuredText and code blocks nested within it.

%files -n python3-rstcheck
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
