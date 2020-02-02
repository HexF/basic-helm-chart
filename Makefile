CHARTINFO = $(shell python chartinfo.py */Chart.yaml $(1))

CHARTNAME := $(call CHARTINFO,name)
CHARTVERSION := $(call CHARTINFO,version)

all: dependencies README.MD out/$(CHARTNAME)-$(CHARTVERSION).tgz

clean: 
	rm README.MD -f
	rm dependencies -f
	rm out -rf

dependencies:
	pip3 install pystache ruamel.yaml
	touch dependencies

README.MD: dependencies README.MD.TEMPLATE $(CHARTNAME)/Chart.yaml $(CHARTNAME)/values.yaml
	python3 makereadme.py README.MD.TEMPLATE README.MD $(CHARTNAME)/Chart.yaml $(CHARTNAME)/values.yaml

out/$(CHARTNAME)-$(CHARTVERSION).tgz: $(CHARTNAME)/ out/
	helm lint $<
	helm package $< -d out/

out/:
	mkdir -p out

	