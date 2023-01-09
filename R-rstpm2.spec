#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rstpm2
Version  : 1.5.9
Release  : 12
URL      : https://cran.r-project.org/src/contrib/rstpm2_1.5.9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rstpm2_1.5.9.tar.gz
Summary  : Smooth Survival Models, Including Generalized Survival Models
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-rstpm2-lib = %{version}-%{release}
Requires: R-BH
Requires: R-Rcpp
Requires: R-RcppArmadillo
Requires: R-bbmle
Requires: R-deSolve
Requires: R-fastGHQuad
BuildRequires : R-BH
BuildRequires : R-Rcpp
BuildRequires : R-RcppArmadillo
BuildRequires : R-bbmle
BuildRequires : R-deSolve
BuildRequires : R-fastGHQuad
BuildRequires : R-ggplot2
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
### rstpm2: An R package for link-based survival models ###
#### NOTE: versions 1.4.1 and 1.4.2 of rstpm2 included a critical bug in the predict function for type in "hr", "hdiff", "meanhr" or "marghr". ####

%package lib
Summary: lib components for the R-rstpm2 package.
Group: Libraries

%description lib
lib components for the R-rstpm2 package.


%prep
%setup -q -n rstpm2
cd %{_builddir}/rstpm2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1673292148

%install
export SOURCE_DATE_EPOCH=1673292148
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rstpm2/CITATION
/usr/lib64/R/library/rstpm2/DESCRIPTION
/usr/lib64/R/library/rstpm2/INDEX
/usr/lib64/R/library/rstpm2/Meta/Rd.rds
/usr/lib64/R/library/rstpm2/Meta/data.rds
/usr/lib64/R/library/rstpm2/Meta/features.rds
/usr/lib64/R/library/rstpm2/Meta/hsearch.rds
/usr/lib64/R/library/rstpm2/Meta/links.rds
/usr/lib64/R/library/rstpm2/Meta/nsInfo.rds
/usr/lib64/R/library/rstpm2/Meta/package.rds
/usr/lib64/R/library/rstpm2/Meta/vignette.rds
/usr/lib64/R/library/rstpm2/NAMESPACE
/usr/lib64/R/library/rstpm2/NEWS.md
/usr/lib64/R/library/rstpm2/R/rstpm2
/usr/lib64/R/library/rstpm2/R/rstpm2.rdb
/usr/lib64/R/library/rstpm2/R/rstpm2.rdx
/usr/lib64/R/library/rstpm2/Rcpp-tests.R
/usr/lib64/R/library/rstpm2/Thumbs.db
/usr/lib64/R/library/rstpm2/aft.aux
/usr/lib64/R/library/rstpm2/aft.pdf
/usr/lib64/R/library/rstpm2/auto/aft.el
/usr/lib64/R/library/rstpm2/auto/math.el
/usr/lib64/R/library/rstpm2/competing_risks.R
/usr/lib64/R/library/rstpm2/data/Rdata.rdb
/usr/lib64/R/library/rstpm2/data/Rdata.rds
/usr/lib64/R/library/rstpm2/data/Rdata.rdx
/usr/lib64/R/library/rstpm2/doc/Introduction.R
/usr/lib64/R/library/rstpm2/doc/Introduction.Rnw
/usr/lib64/R/library/rstpm2/doc/Introduction.pdf
/usr/lib64/R/library/rstpm2/doc/SimpleGuide.R
/usr/lib64/R/library/rstpm2/doc/SimpleGuide.Rnw
/usr/lib64/R/library/rstpm2/doc/SimpleGuide.pdf
/usr/lib64/R/library/rstpm2/doc/index.html
/usr/lib64/R/library/rstpm2/doc/multistate.Rnw
/usr/lib64/R/library/rstpm2/doc/multistate.pdf
/usr/lib64/R/library/rstpm2/doc/predictnl.R
/usr/lib64/R/library/rstpm2/doc/predictnl.Rnw
/usr/lib64/R/library/rstpm2/doc/predictnl.pdf
/usr/lib64/R/library/rstpm2/fig1-README.md.jpg
/usr/lib64/R/library/rstpm2/fig2-README.md.jpg
/usr/lib64/R/library/rstpm2/help/AnIndex
/usr/lib64/R/library/rstpm2/help/aliases.rds
/usr/lib64/R/library/rstpm2/help/paths.rds
/usr/lib64/R/library/rstpm2/help/rstpm2.rdb
/usr/lib64/R/library/rstpm2/help/rstpm2.rdx
/usr/lib64/R/library/rstpm2/html/00Index.html
/usr/lib64/R/library/rstpm2/html/R.css
/usr/lib64/R/library/rstpm2/include/aft.h
/usr/lib64/R/library/rstpm2/include/c_optim.h
/usr/lib64/R/library/rstpm2/include/gsm.h
/usr/lib64/R/library/rstpm2/include/splines.h
/usr/lib64/R/library/rstpm2/math.aux
/usr/lib64/R/library/rstpm2/math.fdb_latexmk
/usr/lib64/R/library/rstpm2/math.fls
/usr/lib64/R/library/rstpm2/math.html
/usr/lib64/R/library/rstpm2/math.input
/usr/lib64/R/library/rstpm2/math.org
/usr/lib64/R/library/rstpm2/math.out
/usr/lib64/R/library/rstpm2/math.toc
/usr/lib64/R/library/rstpm2/model.bug
/usr/lib64/R/library/rstpm2/pstpm2.out
/usr/lib64/R/library/rstpm2/test.do
/usr/lib64/R/library/rstpm2/tests/testthat.R
/usr/lib64/R/library/rstpm2/tests/testthat/test_base.R
/usr/lib64/R/library/rstpm2/tests/testthat/test_delayed.R
/usr/lib64/R/library/rstpm2/tests/testthat/test_markov_msm.R
/usr/lib64/R/library/rstpm2/tests/testthat/test_missing.R
/usr/lib64/R/library/rstpm2/tests/testthat/test_vuniroot.R
/usr/lib64/R/library/rstpm2/tests/testthat/test_zeroModel.R
/usr/lib64/R/library/rstpm2/tutorial/auto/timevar.el
/usr/lib64/R/library/rstpm2/tutorial/haz_1.png
/usr/lib64/R/library/rstpm2/tutorial/hazz_1.png
/usr/lib64/R/library/rstpm2/tutorial/histo_1.png
/usr/lib64/R/library/rstpm2/tutorial/histo_2.png
/usr/lib64/R/library/rstpm2/tutorial/surv_1.png
/usr/lib64/R/library/rstpm2/tutorial/surv_1_age.png
/usr/lib64/R/library/rstpm2/tutorial/surv_5_age.png
/usr/lib64/R/library/rstpm2/tutorial/timevar.html
/usr/lib64/R/library/rstpm2/tutorial/timevar.org
/usr/lib64/R/library/rstpm2/tutorial/timevar.pdf
/usr/lib64/R/library/rstpm2/tutorial/timevar2.html
/usr/lib64/R/library/rstpm2/tvc-cox.R
/usr/lib64/R/library/rstpm2/unitTests/runTests.R
/usr/lib64/R/library/rstpm2/unitTests/runit.Basic.R
/usr/lib64/R/library/rstpm2/working_code.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/rstpm2/libs/rstpm2.so
/usr/lib64/R/library/rstpm2/libs/rstpm2.so.avx2
/usr/lib64/R/library/rstpm2/libs/rstpm2.so.avx512
