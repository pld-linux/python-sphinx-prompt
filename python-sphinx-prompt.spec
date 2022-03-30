#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx directive to add unselectable prompt
Summary(pl.UTF-8):	Dyrektywa Sphinksa do dodawania pytań bez możliwości wyboru
Name:		python-sphinx-prompt
# keep 1.4.x here for python2 support
Version:	1.4.0
Release:	5
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-prompt/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-prompt/sphinx-prompt-%{version}.tar.gz
# Source0-md5:	4b217991abf068ce9e22cf10393faf56
URL:		http://github.com/sbrunner/sphinx-prompt
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 2
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sphinx directive to add unselectable prompt.

%description -l pl.UTF-8
Dyrektywa Sphinksa do dodawania pytań bez możliwości wyboru.

%package -n python3-sphinx-prompt
Summary:	Sphinx directive to add unselectable prompt
Summary(pl.UTF-8):	Dyrektywa Sphinksa do dodawania pytań bez możliwości wyboru
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-sphinx-prompt
Sphinx directive to add unselectable prompt.

%description -n python3-sphinx-prompt -l pl.UTF-8
Dyrektywa Sphinksa do dodawania pytań bez możliwości wyboru.

%prep
%setup -q -n sphinx-prompt-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/sphinx-prompt
%{py_sitescriptdir}/sphinx_prompt-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-sphinx-prompt
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/sphinx-prompt
%{py3_sitescriptdir}/sphinx_prompt-%{version}-py*.egg-info
%endif
