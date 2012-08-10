Summary:	Password checking library
Summary(es.UTF-8):	Biblioteca de chequeo de contraseñas
Summary(fr.UTF-8):	Bibliothèque de vérification de mots de passe
Summary(pl.UTF-8):	Biblioteka sprawdzania haseł
Summary(pt_BR.UTF-8):	Biblioteca de checagem de senhas
Summary(ru.UTF-8):	Библиотека проверки паролей
Summary(tr.UTF-8):	Parola denetim kitaplığı
Summary(uk.UTF-8):	Бібліотека перевірки паролів
Name:		cracklib
Version:	2.8.19
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://downloads.sourceforge.net/cracklib/%{name}-%{version}.tar.gz
# Source0-md5:	ca0ec168d9c6466612204e8dfb2df8a9
Source1:	ftp://ftp.debian.org/debian/pool/main/c/cracklib2/%{name}2_%{version}-1.debian.tar.gz
# Source1-md5:	12936e97cc34a28f2efec62e115a60e1
URL:		http://sourceforge.net/projects/cracklib/
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	words
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
%pyrequires_eq	python-libs

%description -n python-cracklib
Python binding for cracklib.

%description -n python-cracklib -l pl.UTF-8
Wiązanie Pythona do crackliba.

%prep
%setup -q -a1

%build
%configure \
	--with-default-dict=%{_datadir}/dict/cracklib_dict
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir},%{_includedir},%{_datadir}/dict}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man{3,8}
cp -p debian/*.3 $RPM_BUILD_ROOT%{_mandir}/man3
cp -p debian/*.8 $RPM_BUILD_ROOT%{_mandir}/man8
# debian specific
rm $RPM_BUILD_ROOT%{_mandir}/man8/update-cracklib.8*

chmod 755 util/cracklib-format

util/cracklib-format $RPM_BUILD_ROOT%{_datadir}/%{name}/cracklib-small | \
util/cracklib-packer $RPM_BUILD_ROOT%{_datadir}/dict/cracklib-small
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/cracklib-small

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/*.{la,a}

# already in file(1) database
%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/cracklib.magic

mv -f $RPM_BUILD_ROOT%{_localedir}/{sl_SI,sl}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
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
%{_mandir}/man8/create-cracklib-dict.8*
%{_libdir}/libcrack.la
%{_includedir}/crack.h
%{_includedir}/packer.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libcrack.a

%files -n python-cracklib
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_cracklibmodule.so
%{py_sitescriptdir}/%{name}.*
