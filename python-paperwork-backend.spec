%global module paperwork-backend

Summary:	Paperwork's backend
Name:		python-%{module}
Version:	2.2.0
Release:	1
License:	GPL-3.0-or-later
Group:		Development/Python
URL:		https://pypi.org/project/paperwork-backend/
Source0:	https://pypi.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
Patch0:		python-paperwork-backend-2.2.0-fix_version_path.patch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(python-levenshtein)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch

%description
This is the backend part of Paperwork.

It manages:
 *  The work directory / Access to the documents
 *  Indexing
 *  Searching
 *  Suggestions
 *  Import
 *  Export

%files
%{py_puresitedir}/paperwork_backend
%{py_puresitedir}/paperwork_backend-*.*-info

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py_install

