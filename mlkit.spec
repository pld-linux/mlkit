Summary:	A Standard ML native compiler
Summary(pl):	Kompilator Standard ML do kodu maszynowego x86
Name:		mlkit
Version:	4.0.0
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.it.edu/research/mlkit/dist/%{name}-%{version}.tgz
URL:		http://www.it.edu/research/mlkit
BuildRequires:	smlnj = 110.0.7
Requires:	%{name}-common = %{version}
ExclusiveArch:	%{ix86}
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# don't strip heap images
%define		no_install_post_strip 1

%description 
The ML Kit (henceforth refered to as the Kit) is a compiler for the
programming language Standard ML. The Kit covers all of Standard ML,
as defined in the 1997 edition of the Definition of Standard ML and
supports most of the Standard ML Basis Library. The Kit uses a region
based memory management scheme in which allocation and de-allocation
primitives are added to the program at compile time. The Kit also
makes it possible to combine the region based memory management scheme
with traditional reference tracing garbage collection. The largest program
compiled with the Kit is the Kit itself (around 80.000 lines of SML,
plus the Basis Library).

This package provides version of compiler which generates effective x86
machine code.

%description -l pl
ML Kit jest kompilatorem dla jêzyka programowania Standard ML. ML Kit
obejmuje kompletny standard SML 97 i wspiera wiêkszo¶æ standardowej
biblioteki SML (Standard ML Basis Library). ML Kit u¿ywa schematu
zarz±dzania pamiêci± bazuj±cego na regionach, w którym operacje alokacji
i dealokacji s± dodawane do programu w trakcie kompilacji. ML Kit umo¿liwia
tak¿e ³±czenie zarz±dzania pamiêci± opartego na regionach ze standardowym
od¶miecaniem ze zliczaniem referencji. Najwiêkszym programem skompilowanym
przez ML Kit jest on sam (oko³o 80000 linii SML plus biblioteka standardowa).

Pakiet tez zawiera wersjê kompilatora generuj±c± efektywny kod dla maszyn
x86.

%package kam
Summary:	A Standard ML bytecode compiler
Summary(pl):	Kompilator Standard ML do przenosnego kodu bajtowego
Group:		Development/Languages
Requires:	%{name}-common = %{version}

%description kam 
The ML Kit (henceforth refered to as the Kit) is a compiler for the
programming language Standard ML. The Kit covers all of Standard ML,
as defined in the 1997 edition of the Definition of Standard ML and
supports most of the Standard ML Basis Library. The Kit uses a region
based memory management scheme in which allocation and de-allocation
primitives are added to the program at compile time. The Kit also
makes it possible to combine the region based memory management scheme
with traditional reference tracing garbage collection. The largest program
compiled with the Kit is the Kit itself (around 80.000 lines of SML,
plus the Basis Library).

This package provides version of compiler which generates portable bytecode
that can be interpreted by an abstract machine.

%description kam -l pl
ML Kit jest kompilatorem dla jêzyka programowania Standard ML. ML Kit
obejmuje kompletny standard SML 97 i wspiera wiêkszo¶æ standardowej
biblioteki SML (Standard ML Basis Library). ML Kit u¿ywa schematu
zarz±dzania pamiêci± bazuj±cego na regionach, w którym operacje alokacji
i dealokacji s± dodawane do programu w trakcie kompilacji. ML Kit umo¿liwia
tak¿e ³±czenie zarz±dzania pamiêci± opartego na regionach ze standardowym
od¶miecaniem ze zliczaniem referencji. Najwiêkszym programem skompilowanym
przez ML Kit jest on sam (oko³o 80000 linii SML plus biblioteka standardowa).

Pakiet tez zawiera wersjê kompilatora generuj±c± przeno¶ny kod bajtowy który
mo¿e byæ interpretowany przez maszynê wirtualn±

%package common
Summary:	Common files for ML Kit bytecode and native compilers
Summary(pl):	Pliki wspólne dla kompilatora natywnego i kodu bajtowego ML Kit
Group:		Development/Languages

%description common
Common files for ML Kit bytecode and native compilers.
Install mlkit or mlkit-kam packages for full ML Kit system.

%description common -l pl
Pliki wspólne dla kompilatora natywnego i kodu bajtowego ML Kit.
Zainstaluj pakiety mlkit lub mlkit-kam dla pe³nego systemu ML Kit.

%prep
%setup -q

%build
%{__make} mlkit
%{__make} mlkit_kam

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_libdir}/mlkit/bin,%{_bindir},%{_examplesdir}}
install bin/{runtimeSystem*.o,kam} $RPM_BUILD_ROOT%{_libdir}/mlkit/bin
install bin/mlkit{,_kam}.x86-linux $RPM_BUILD_ROOT%{_libdir}/mlkit/bin
install bin/rp2ps $RPM_BUILD_ROOT%{_bindir}
cp -a basislib ml-yacc-lib $RPM_BUILD_ROOT%{_libdir}/mlkit
cp -a kitdemo $RPM_BUILD_ROOT%{_examplesdir}/mlkit-%{version}
(cd $RPM_BUILD_ROOT && ln -sf %{_bindir}/rp2ps .%{_libdir}/mlkit/bin/rp2ps)

cat << EOF > $RPM_BUILD_ROOT%{_bindir}/mlkit
#!/bin/sh
%{_prefix}/lib/mlkit/bin/mlkit.x86-linux %{_libdir}/mlkit $*
EOF
cat << EOF > $RPM_BUILD_ROOT%{_bindir}/mlkit_kam
#!/bin/sh
%{_prefix}/lib/mlkit/bin/mlkit_kam.x86-linux %{_libdir}/mlkit $*
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rp2ps
%attr(755,root,root) %{_bindir}/mlkit
%attr(755,root,root) %{_libdir}/mlkit/bin/mlkit.x86-linux
%attr(755,root,root) %{_libdir}/mlkit/bin/rp2ps
%{_libdir}/mlkit/bin/runtimeSystem*.o

%files kam
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mlkit_kam
%attr(755,root,root) %{_libdir}/mlkit/bin/kam
%attr(755,root,root) %{_libdir}/mlkit/bin/mlkit_kam.x86-linux

%files common
%defattr(644,root,root,755)
%doc README NEWS doc/manual/mlkit.pdf
%{_libdir}/mlkit/ml-yacc-lib
%{_libdir}/mlkit/basislib
%{_examplesdir}/mlkit-%{version}
