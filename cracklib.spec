#
# Conditional build:
%bcond_without	python2		# CPython 2 bindings
%bcond_without	python3		# CPython 3 bindings
%bcond_without	static_libs	# static library

Summary:	Password checking library
Summary(es.UTF-8):	Biblioteca de chequeo de contraseñas
Summary(fr.UTF-8):	Bibliothèque de vérification de mots de passe
Summary(pl.UTF-8):	Biblioteka sprawdzania haseł
Summary(pt_BR.UTF-8):	Biblioteca de checagem de senhas
Summary(ru.UTF-8):	Библиотека проверки паролей
Summary(tr.UTF-8):	Parola denetim kitaplığı
Summary(uk.UTF-8):	Бібліотека перевірки паролів
Name:		cracklib
Version:	2.10.2
Release:	4
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/cracklib/cracklib/releases
Source0:	https://github.com/cracklib/cracklib/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	a99e0aef4c677df7063624690b634988
Patch0:		python-flags.patch
URL:		https://github.com/cracklib/cracklib
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	libtool >= 2:2
%{?with_python2:BuildRequires:	python-devel >= 2}
%{?with_python2:BuildRequires:	python-modules >= 2}
%{?with_python3:BuildRequires:	python3-devel >= 1:3.2}
%{?with_python3:BuildRequires:	python3-modules >= 1:3.2}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.043
BuildRequires:	tar >= 1:1.22
BuildRequires:	words
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
CrackLib tests passwords to determine whether they match certain
security-oriented characteristics. You can use CrackLib to stop users
from choosing passwords which would be easy to guess. CrackLib
performs certain tests:

- It tries to generate words from a username and gecos entry and
  checks those words against the password;
- It checks for simplistic patterns in passwords;
- It checks for the password in a dictionary.

CrackLib is actually a library containing a particular C function
which is used to check the password, as well as other C functions.
CrackLib is not a replacement for a passwd program; it must be used in
conjunction with an existing passwd program.

Install the cracklib package if you need a program to check users'
passwords to see if they are at least minimally secure. If you install
CrackLib, you'll also want to install the cracklib-dicts package.

%description -l de.UTF-8
Überprüft Paßwörter auf Sicherheitsmerkmale - Länge, Eindeutigkeit,
Anwesenheit in einer Wörter-Datenbank usw.

%description -l fr.UTF-8
Vérifie les caractéristiques liées à la sécurité des mots de passe -
longueur, unicité, s'ils sont dans une base de mots, etc.

%description -l pl.UTF-8
CrackLib sprawdza hasła pod kątem bezpieczeństwa. Można użyć tej
biblioteki do powstrzymywania użytkowników przed wybieraniem haseł
łatwych do odgadnięcia. CrackLib przeprowadza następujące testy:

- próbuje wygenerować słowa z nazwy użytkownika i wpisu gecos, a
  następnie porównuje je z hasłem
- szuka prostych wzorców w haśle
- szuka hasła w słowniku

CrackLib to biblioteka zawierająca funkcję C służącą do sprawdzania
hasła oraz inne funkcje C. Nie jest to zamiennik programu passwd -
musi być użyty w połączeniu z istniejącym programem passwd.

%description -l pt_BR.UTF-8
Inclui os dicionários cracklib para o padrão /usr/dict/words, assim
como os utilitários necessários para criar dicionários.

%description -l ru.UTF-8
CrackLib проверяет пароли на предмет соответствия некоторым критериям
безопасности. Она может быть использована для предотвращения выбора
пользователями легкоугадываемых паролей. CrackLib производит такие
тесты:

- Генерирует слова из имени пользователя и поля gecos и сравнивает их
  с паролем;
- Ищет в паролях простые шаблоны;
- Проверяет пароль на наличие его в словаре.

CrackLib - это, собственно, библиотека, содержащая специфическую
функцию C для угадывания паролей и некоторые другие функции. Это не
замена программы passwd, ее надо использовать совместно с существующей
программой passwd.

%description -l tr.UTF-8
Parolaların uzunlukları, sistemde tek olmaları, sözcük veri tabanında
bulunmamaları gibi güvenlikle ilgili özelliklerini kontrol eder.

%description -l uk.UTF-8
CrackLib перевіряє паролі на відповідність деяким критеріям безпеки.
Вона може бути використана для запобігання вибору користувачами
паролів, які легко відгадати. Вона виконує такі тести:

- Генерує слова з імені користувача та поля gecos і порівнює їх з
  паролем;
- Шукає в паролях прості шаблони;
- Перевіряє паролі на наявність їх у словнику.

CrackLib - це, власне, бібліотека, що містить специфічну функцію C для
відгадування паролів та деякі інші функції. Це не заміна програми
passwd, її треба використовувати спільно з існуючою програмою passwd.

%package devel
Summary:	Header files and documentation for cracklib
Summary(es.UTF-8):	Archivos de inclusión y bibliotecas para cracklib
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja dla cracklib
Summary(pt_BR.UTF-8):	Arquivos de inclusão e bibliotecas para a cracklib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and documentation for cracklib.

%description devel -l es.UTF-8
Este paquete contiene los archivos de inclusión y bibliotecas que se
necesitan para desarrollar programas que usan cracklib.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja dla cracklib.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos de inclusão e bibliotecas que são
necessários para desenvolver programas que usam a cracklib.

%package static
Summary:	Static cracklib library
Summary(pl.UTF-8):	Statyczna biblioteka cracklib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static cracklib library.

%description static -l pl.UTF-8
Statyczna biblioteka cracklib.

%package -n python-cracklib
Summary:	Python binding for cracklib
Summary(pl.UTF-8):	Wiązanie Pythona do crackliba
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-libs >= 2

%description -n python-cracklib
Python binding for cracklib.

%description -n python-cracklib -l pl.UTF-8
Wiązanie Pythona do crackliba.

%package -n python3-cracklib
Summary:	Python binding for cracklib
Summary(pl.UTF-8):	Wiązanie Pythona do crackliba
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3-libs >= 1:3.2

%description -n python3-cracklib
Python binding for cracklib.

%description -n python3-cracklib -l pl.UTF-8
Wiązanie Pythona do crackliba.

%prep
%setup -q
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%define	configuredir	..
%if %{with python2}
install -d build-python2
cd build-python2
%configure \
	PYTHON=%{__python} \
	--disable-static \
	--with-default-dict=%{_datadir}/dict/cracklib_dict

%{__make}
cd ..
%endif

install -d build
cd build
%configure \
	PYTHON=%{__python3} \
	%{__enable_disable static_libs static} \
	--with-default-dict=%{_datadir}/dict/cracklib_dict \
	%{!?with_python3:--without-python}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir},%{_includedir},%{_datadir}/dict}

%if %{with python2}
%{__make} -C build-python2 install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

chmod 755 util/cracklib-format

util/cracklib-format $RPM_BUILD_ROOT%{_datadir}/%{name}/cracklib-small | \
build/util/cracklib-packer $RPM_BUILD_ROOT%{_datadir}/dict/cracklib-small
%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/cracklib-small

%if %{with python2}
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/*.la
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/test_cracklib.py*
%py_postclean
%endif

%if %{with python3}
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/*.la
%{?with_static_libs:%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/*.a}
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/test_cracklib.py*
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/__pycache__/test_cracklib.*.py*
%endif

# already in file(1) database
%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/cracklib.magic

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README README-DAWG README-LICENSE README-WORDS
%attr(755,root,root) %{_libdir}/libcrack.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcrack.so.2
%{_datadir}/dict/cracklib-small.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/cracklib-*
%attr(755,root,root) %{_sbindir}/create-cracklib-dict
%attr(755,root,root) %{_libdir}/libcrack.so
%{_mandir}/man3/FascistCheck.3*
%{_mandir}/man8/cracklib-check.8*
%{_mandir}/man8/cracklib-format.8*
%{_mandir}/man8/cracklib-update.8*
%{_mandir}/man8/create-cracklib-dict.8*
%{_libdir}/libcrack.la
%{_includedir}/crack.h
%{_includedir}/packer.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcrack.a
%endif

%if %{with python2}
%files -n python-cracklib
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_cracklib.so
%{py_sitescriptdir}/cracklib.py[co]
%endif

%if %{with python3}
%files -n python3-cracklib
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/_cracklib.so
%{py3_sitescriptdir}/cracklib.py
%{py3_sitescriptdir}/__pycache__/cracklib.*.py[co]
%endif
