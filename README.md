# NCP-ARI Study Notes

Folder naming: `<section>.T<n>` = exam topic, `<section>.SR<n>` = suggested reading, `<section>.O<n>` = other/extra material.

After adding or moving a note, run `python3 tools/build_nav.py` to refresh the navbar on every page.

## AI Infrastructure Basics for Data Centers - 20%

This section covers AI infrastructure basics, focusing on verifying data center power and cooling capacity, distinguishing AC/DC racks, balancing rPDUs, checking power redundancy and grounding, and understanding various cooling systems.


### Potential Exam Topics:
- **T1** Verify power and cooling capacity in the data center.
  - [Power in, heat out: data center capacity](1.T1/datacenter-power-cooling-guide.html)
  - [No raised floor? Cooling on a slab](1.T1/datacenter-cooling-no-raised-floor.html)
  - [Direct-to-chip cooling](1.T1/datacenter-direct-to-chip-cooling.html)
  - [GB200 NVL72: power and cooling](1.T1/datacenter-gb200-nvl72-guide.html)
  - [Data center formulas](1.T1/datacenter-formulas-guide.html)

- **T2** Describe the difference between AC- and DC-powered racks.
  - [AC vs DC powered racks](1.T2/ac-vs-dc-racks.html)
  - https://claude.ai/share/1f2118d7-2c21-4c45-9b82-def8652c4b7a


- **T3** Balance the rPDUs for AC-powered racks.
  - [Balancing rack PDUs on AC racks](1.T3/balance-rpdus.html)


- **T4** Verify power redundancy per rack.
  - [Verifying power redundancy per rack](1.T4/rack-power-redundancy.html)
- **T5** Verify the power capacity by PDU type.
  - [Verifying power capacity by PDU type](1.T5/pdu-power-capacity.html)
- **T6** Describe CDUs for liquid-cooled racks.
  - [CDUs for liquid-cooled racks](1.T6/cdus-liquid-cooled-racks.html)
- **T7** Verify grounding.
  - [Verifying grounding](1.T7/verify-grounding.html)
- **T8** Differentiate between hot-aisle and cold-aisle cooling.
  - [Hot aisle vs. cold aisle](1.T8/hot-vs-cold-aisle.html)

### Suggested Readings

**SR1** Improving Data Center Cooling With Cold Aisle Containment
- [Cold aisle containment, explained](1.SR1/cold-aisle-containment.html) · [Test](1.SR1/cold-aisle-containment-test.html)

**SR2** 380 Vdc Architectures for the Modern Data Center
https://datacenters.lbl.gov/sites/default/files/380VdcArchitecturesfortheModernDataCenter.pdf
- [380 Vdc architectures, explained](1.SR2/380Vdc_Architectures_Explained.html)

https://claude.ai/share/42120fc0-722c-4f72-980b-788a4ff8ee53

**SR3** What Is an Intelligent PDU?
https://www.vertiv.com/en-cn/about/news-and-events/articles/educational-articles/what-is-an-intelligent-pdu/
https://claude.ai/share/2cfdb354-cc0f-4d52-b6ad-16baf20b2d85
- [Intelligent PDUs, explained](1.SR3/intelligent-pdu-explained.html)

**SR4** 3-Phase Power Explained
https://synaccess.com/resources/3-phase-power-explained
https://claude.ai/share/02a30952-821c-4003-9f0d-243a59b5e6c6
- [3-phase power, illustrated](1.SR4/3-phase-power-explained.html)

**SR5** Alternating Phase
https://cdn10.servertech.com/assets/documents/documents/823/original/Alternating_Phase_New_Look.pdf?1565385050
- [Alternating phase PDUs, explained](1.SR5/alternating-phase-explained.html)


**SR6** Coolant Distribution Units (CDUs) for Data Center Cooling | nVent
- [nVent CDU, explained](1.SR6/nvent-cdu-explained.html)

**SR7** How to Properly Ground Your Server Rack
- [Grounding a server rack, explained](1.SR7/server-rack-grounding.html)

**SR8** National Electric Code
- [NFPA codes & standards list, explained](1.SR8/nfpa-codes-explained.html)

**SR9** Delay and Power Calculation Standards
- [SDF explained: IEC 61523-3 / IEEE 1497](1.SR9/sdf-explained.html)

**SR10** TC 9.9 Data Center Environmental Guidelines

**SR11** CRAC With Aisle Containment: Traditional Data Center Cooling Guide
- [CRAC with aisle containment, explained](1.SR11/crac-aisle-containment-explained.html)

### Other

**O1** Extra material
- [How AI changes data center design (Schneider WP110)](1.O1/ai-datacenter-explainer.html)
- [Liquid cooling architectures for AI data centers](1.O1/liquid-cooling-explainer.html)
- [Regulation (EU) 2019/424: servers and data storage](1.O1/eu-2019-424-servers-storage-explained.html)



## Pre-Deployment Planning and Site Assessment for AI Data Centers - 11%
This exam section covers pre-deployment planning, including physical network documentation, site surveys for load capacity, and verifying environmental readiness (power, cooling, thermal zones) for AI infrastructure.

### Potential Exam Topics:
- **T1** Describe physical network design documentation.
  - [Physical network design documentation](2.T1/physical-network-design-docs.html)
- **T2** Conduct site surveys for cable management infrastructure (load capacity, clearances).
  - [Site survey for cable management infrastructure](2.T2/cable-pathway-site-survey.html)
- **T3** Verify environmental readiness (rack spacing, power, cooling, thermal zones).
  - [Verifying environmental readiness](2.T3/environmental-readiness.html)
- **T4** Describe inventory check procedures.
  - [Inventory check procedures](2.T4/inventory-check-procedures.html)

### Suggested Readings

**SR1** ANSI/TIA-606-B Explained: The Data Center Cable Labeling Standard That Keeps Chaos in Check
- [TIA-606-B cable labeling, explained visually](2.SR1/tia-606b-cable-labeling-explained.html)

**SR2** Enhanced Efficiency in Data Center With Elevated Return Air Temperature
- [Elevated return air temperature, explained](2.SR2/elevated_return_air_explainer.html)

**SR3** 392.18(F) Cable Tray Access
- [NEC 392.18(F) cable tray access, explained](2.SR3/nec-392-18F-cable-tray-access.html)

**SR4** What Is the Difference Between an 80% Rated Breaker and a 100% Rated Breaker?
- [80% vs 100% rated breakers, explained](2.SR4/breaker-80-vs-100-explained.html)

**SR5** Manage Airflow for Cooling Efficiency | ENERGY STAR

**SR6** Implementing Data Center Cooling Best Practices

**SR7** Move to a Hot Aisle/Cold Aisle Layout | ENERGY STAR
- [Hot aisle / cold aisle layout, explained](2.SR7/hot-aisle-cold-aisle-explained.html)

**SR8** Networking Solutions for the Era of AI | NVIDIA
- [NVIDIA networking, explained](2.SR8/nvidia-networking-explained.html)



## Rack Infrastructure Preparation for AI Platforms - 10%
This section covers preparing rack infrastructure for AI platforms, focusing on extra-wide rack specifications, cable management, EMI mitigation for power/data pathways, and verifying containment clearances.

### Potential Exam Topics:
- **T1** Describe extra-wide racks for AI platforms.
- **T2** Install cable management accessories (vertical/horizontal ducts, bend radius managers).
- **T3** Coordinate power and data cable pathways (EMI mitigation).
- **T4** Verify rack containment clearance (front-post to front door and front-post to rear-post or inter-rack posts).

### Suggested Readings

**SR1** Best Practices Guide for Energy-Efficient Data Center Design
- [Energy-efficient data center design (NREL guide), explained](3.SR1/data-center-design-explained.html)

**SR2** NVIDIA DGX™ H100/H200 System User Guide
- [DGX H100/H200 user guide, explained](3.SR2/dgx-h100-h200-guide-explained.html)

**SR3** InfiniBand Cables Explained: HDR vs NDR, QSFP56 vs OSFP, DAC vs AOC
- [InfiniBand cables, explained visually](3.SR3/infiniband-cables-explained.html)

**SR4** Wyr-Grid Overhead Cable Tray Routing System
- [Wyr-Grid overhead cable tray, explained](3.SR4/wyr-grid-explained.html)

**SR5** NFPA 70 (NEC) Code Development
- [NFPA 70 (NEC) code development, explained](3.SR5/nfpa70-explained.html)

**SR6** Cisco Nexus Installation Guide
- [Nexus 93180YC-FX: preparing the site](3.SR6/n93180ycfx-site-prep.html)

**SR7** Rack Cooling Systems | Vertiv Thermal Management
- [Vertiv rack cooling, explained](3.SR7/vertiv-rack-cooling-explained.html)
- [Vertiv rack cooling, explained (v2)](3.SR7/vertiv-rack-cooling-explained2.html)

**SR8** Server Rack Cabinet Compatibility Guide
- [Will this server fit this rack? Intel guide, explained](3.SR8/intel-rack-compatibility-explained.html)
- [Intel rack cabinet compatibility guide, explained](3.SR8/intel_rack_compatibility_explained.html)



## High-Density Cabling Installation for AI Clusters - 30%
This section details the practical deployment of high-density cables. It covers distinguishing between NVIDIA and other cables, understanding transceiver form factors (OSFP/QSFP) and fiber types (MMF/SMF), deploying InfiniBand copper and MPO/APC fiber optic cables, implementing the 50/50 left-right routing strategy, and applying professional cable management practices, including cleaning connectors.

### Potential Exam Topics:
- **T1** Describe the difference between NVIDIA cables vs. others.
  - [NVIDIA cables vs. everyone else's](4.T1/nvidia-vs-other-cables.html)
- **T2** Describe the different transceiver form factors (OSFP vs. QSFP).
  - [OSFP vs. QSFP: same lanes, different boxes](4.T2/osfp-vs-qsfp-form-factors.html)
- **T3** Describe the difference between MMF and SMF.
  - [Multimode vs. single-mode fiber](4.T3/mmf-vs-smf.html)
- **T4** Describe the transceiver requirements across the various SMF distances.
  - [Picking single-mode optics by distance](4.T4/smf-transceiver-distances.html)
- **T5** Deploy InfiniBand NDR/XDR copper cables.
  - [Deploying NDR/XDR copper cables](4.T5/infiniband-copper-cables.html)
- **T6** Install MPO/APC fiber optic cables.
  - [Installing MPO/APC fiber](4.T6/mpo-apc-fiber-install.html)
- **T7** Implement 50/50 left-right cable routing strategy.
  - [The 50/50 left-right routing strategy](4.T7/50-50-cable-routing.html)
- **T8** Bundle and dress cables professionally (hook and loop fasteners, soft ties, color coding).
  - [Bundling and dressing cables professionally](4.T8/bundle-and-dress-cables.html)
- **T9** Install fiber optic transceivers and clean connectors.
  - [Installing transceivers and cleaning connectors](4.T9/install-transceivers-clean-connectors.html)

### Suggested Readings and Recommended Training for High-Density Cabling Installation

**SR1** Cable Validation Tool (CVT) Fundamentals: free self-paced course

**SR2** Choosing Between OSFP and QSFP-DD: Key Considerations for 800G Optical Transceivers
- [OSFP vs QSFP-DD for 800G, explained](4.SR2/osfp-vs-qsfpdd-explained.html)

**SR3** Cable Management Best Practices—NVIDIA DGX SuperPOD™
- [Cable management best practices, explained](4.SR3/cable-management-best-practices.html)

**SR4** Deploying the Bundles—NVIDIA DGX SuperPOD: Cabling Data Centers Design Guide
- [Deploying the bundles, explained](4.SR4/deploying-the-bundles-explained.html)

**SR5** Maintaining NDR Connectors and Cables—NVIDIA DGX SuperPOD
- [Keeping NDR optics clean](4.SR5/ndr-connector-maintenance-explained.html)

**SR6** Connectors and Cages
- [Connectors and cages, explained (NVIDIA LinkX)](4.SR6/nvidia-connectors-and-cages.html)

**SR7** Validated and Supported Cables and Switches—NVIDIA Docs
- [ConnectX-7 validated cables & switches, explained](4.SR7/connectx7-cables-explained.html)

**SR8** NVIDIA Q32xx and Q34xx XDR 800 Gb/s InfiniBand Switch Systems User Manual
- [Reading the LEDs on Q32xx / Q34xx XDR switches](4.SR8/nvidia-xdr-switch-led-guide.html)

**SR9** How to Understand OSFP vs. QSFP-DD Form Factors—BYXGD
- [OSFP vs QSFP-DD, explained visually](4.SR9/osfp-vs-qsfp-dd-explained.html)

**SR10** 200G Optical Transceiver: QSFP‑DD vs. OSFP for Data Centers
- [200G transceivers: QSFP-DD vs OSFP, explained](4.SR10/200g-qsfp-dd-vs-osfp-explained.html)

**SR11** Single Mode vs. Multimode Fiber: A Complete Comparison Guide
- [Single-mode vs multimode fiber, explained visually](4.SR11/single-mode-vs-multimode-fiber2.html)

**SR12** Single-Mode vs. Multimode Fiber: A Comprehensive Guide
- [Single-mode vs multimode fiber, explained](4.SR12/single-mode-vs-multimode-fiber.html)

**SR13** 2 Big Mistakes to Avoid During Fiber Cable Installation
- [Two big mistakes in fiber installation](4.SR13/fiber-installation-mistakes.html)

**SR14** Single-Mode vs. Multimode Fiber—DCD
- [Single-mode vs multimode fiber (DCD), explained](4.SR14/single-mode-vs-multimode-fiber3.html)

**SR15** Cleaning and Inspecting MPO/MTP Connectors | Fluke Networks
- [Cleaning and inspecting MPO/MTP connectors](4.SR15/mpo-mtp-cleaning-inspection.html)

**SR16** The Fiber Optic Association, Inc.
- [Fiber optic installation — FOA guide](4.SR16/foa-fiber-installation-explained.html)

**SR17** Installing an OSFP Transceiver
- [Installing an OSFP transceiver — visual guide](4.SR17/osfp-transceiver-install.html)

**SR18** Clean & Inspect: What IEC 61300-3-35 Means to You | MicroCare
- [Clean & inspect — IEC 61300-3-35 explained](4.SR18/iec-61300-3-35-explained.html)



## Cable Support Systems and Weight Management - 7%
This section covers defining a team orientation plan for the cabling workflow, designing cable support systems for ultra-high-density loads, installing overhead cable support infrastructure, and implementing cable slack management.

### Potential Exam Topics:
- **T1** Define a team orientation plan for the cabling workflow.
- **T2** Design cable support systems for ultra-high-density loads.
- **T3** Install overhead cable support infrastructure.
- **T4** Implement cable slack management.
- **T5** Understand the causes of unexpected visual results.
- **T6** Update the extent attribute of a mesh after updating its points.

> T5 and T6 appear this way on NVIDIA's exam page but look like a copy-paste error from another exam.

### Suggested Readings

**SR1** Networking—NVIDIA DGX SuperPOD: Data Center Design Featuring NVIDIA DGX H100 Systems
- [DGX SuperPOD H100 networking: cables, trays and load](5.SR1/dgx-superpod-h100-networking-explained.html)

**SR2** Cable Installation and Management Guidelines—NVIDIA Docs
- [Cable installation & management, explained](5.SR2/nvidia-cable-guidelines-explained.html)

**SR3** The Fiber Optic Association, Inc.
- [Fiber optic installation — FOA technical bulletin](5.SR3/fiber-optic-installation-explained3.html)

**SR4** The FOA Reference for Fiber Optics-Installing Fiber Optic Cable
- [Installing fiber optic cable — visual explainer](5.SR4/fiber-cable-installation-explained.html)
- [Installing fiber optic cable — explained](5.SR4/fiber-cable-installation-explained2.html)



## Testing, Verification, and Documentation for AI Cabling - 12%
This section covers cable continuity/link testing, final quality inspection (bend radius, labeling, airflow), documentation with diagrams and photos, and troubleshooting signal integrity issues like BER.

### Potential Exam Topics:
- **T1** Perform cable continuity and link testing (optical power meter, link status, differentiate between NVIDIA vs. non-NVIDIA cabling).
  - [Continuity and link testing](6.T1/continuity-and-link-testing.html)
- **T2** Conduct final deployment quality inspection (bend radius, labeling, airflow).
  - [Final deployment quality inspection](6.T2/final-quality-inspection.html)
- **T3** Document cable deployment with photos and as-built diagrams.
  - [Documenting the cable deployment](6.T3/document-as-built.html)
- **T4** Troubleshoot signal integrity issues (dirty connectors, over-bending, BER, link down vs. high BER issues).
  - [Troubleshooting signal integrity](6.T4/signal-integrity-troubleshooting.html)

### Suggested Readings

**SR1** Diagnosing OTDR Test Failures—DTX Compact OTDR Module | Fluke Networks
- [Diagnosing OTDR test failures, explained](6.SR1/otdr-test-failures-explained.html)

**SR2** Contaminants Such as Dust on Fiber Optic Connector End Face Cause Poor IO Performance
- [Dirty fiber connectors and poor I/O performance](6.SR2/fiber-connector-contamination-explained.html)

**SR3** NVIDIA Cumulus™ Linux User Guide
- [Troubleshooting Layer 1 on Cumulus Linux](6.SR3/cumulus-layer1-troubleshooting-explained.html)

**SR4** OTDR—Optical Time Domain Reflectometer | Fluke Networks



## Safety, Standards, and Compliance for Data Centers - 10%
This section covers adhering to electrical safety, LOTO, fire compliance, NVIDIA installation standards, and proper ESD protection within high-power data center environments.

### Potential Exam Topics:
- **T1** Adhere to electrical safety practices (LOTO, PPE, 120 kW+ environments).
- **T2** Comply with fire safety and cable flame ratings (NEC plenum requirements).
- **T3** Follow NVIDIA-specific installation standards (DU-10438, warranty compliance).
- **T4** Implement ESD protection for sensitive components.

### Suggested Readings

**SR1** Lockout-Tagout Procedures in 8 Steps
- [Lockout–tagout in 8 steps, explained](7.SR1/loto-8-steps-explained.html)

**SR2** The 7 Steps in a LOTO Procedure: What Are They, and How Do They Work?

**SR3** The Role of CMP and CMR Cables in Data Centers and Office Buildings

**SR4** Fire-Rated Cable Guide: Understanding CM, CMR, and CMP Standards | Wonderful Group

**SR5** Data Center Humidity: ASHRAE Standards, ESD Risks, and System Selection

**SR6** Cisco Optical Transceiver Handling Guide
