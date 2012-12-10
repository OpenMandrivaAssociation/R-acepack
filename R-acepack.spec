%global packname  acepack
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.3_3.0
Release:          1
Summary:          ace() and avas() for selecting regression transformations
Group:            Sciences/Mathematics
License:          MIT + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-3.0.tar.gz
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
%rename R-cran-acepack

%description
ACE and AVAS methods for choosing regression transformations.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3_3.0-1
+ Revision: 775014
- Update to latest version

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3_2.3-1
+ Revision: 774778
- Update and rebuild with R2spec
- Update and rebuild with R2spec

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.2.2-7mdv2011.0
+ Revision: 616443
- the mass rebuild of 2010.0 packages

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 1.3.2.2-6mdv2010.0
+ Revision: 433067
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.3.2.2-5mdv2009.0
+ Revision: 260118
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.3.2.2-4mdv2009.0
+ Revision: 248007
- rebuild

* Fri Feb 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.2.2-2mdv2008.1
+ Revision: 176959
- remove requires on libR.so

* Sun Feb 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.2.2-1mdv2008.1
+ Revision: 169980
- complete spec file
- fix Url
- add source and spec file
- Created package structure for R-cran-acepack.

