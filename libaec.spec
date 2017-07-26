Name:           libaec
Version:        1.0.1
Release:        2%{?dist}
Summary:        Adaptive Entropy Coding library
License:        BSD
Url:            https://gitlab.dkrz.de/k202009/libaec
Source:         https://gitlab.dkrz.de/k202009/libaec/repository/archive.tar.gz?ref=v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake

%description
Libaec provides fast loss-less compression of 1 up to 32 bit wide
signed or unsigned integers (samples). The library achieves best
results for low entropy data as often encountered in space imaging
instrument data or numerical model output from weather or climate
simulations. While floating point representations are not directly
supported, they can also be efficiently coded by grouping exponents
and mantissa.

Libaec implements Golomb Rice coding as defined in the Space Data
System Standard documents 121.0-B-2 and 120.0-G-2.

Libaec includes a free drop-in replacement for the SZIP
library (http://www.hdfgroup.org/doc_resource/SZIP).

%package devel
Summary:        Devel package for libaec (Adaptive Entropy Coding library)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Devel files for libaec (Adaptive Entropy Coding library).

%prep
%setup -q -T -a 0 -c
mv %{name}-v%{version}-*/* .

%build
mkdir build
pushd build
%cmake ..
%make_build
popd

%install
%make_install -C build

%check
#test data missing in tarball for check_szcomp and sampledata.sh
make -C build test ARGS="-E \(check_szcomp\|sampledata.sh\)"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md README.SZIP CHANGELOG.md
%license Copyright.txt doc/patent.txt
%{_bindir}/aec
%{_libdir}/lib*.so.*
%{_mandir}/man1/aec.*

%files devel
%{_includedir}/*.h
%{_libdir}/lib*.so

%changelog
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Christoph Junghans <junghans@votca.org> - 1.0.1-1
- version bump to 1.0.1 - bug #1471766

* Wed Jun 21 2017 Christoph Junghans <junghans@votca.org> - 1.0.0-2
- comments from review #1462443

* Sat Jun 17 2017 Christoph Junghans <junghans@votca.org> - 1.0.0-1
- initial import
