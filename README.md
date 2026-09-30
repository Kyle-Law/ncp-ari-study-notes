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


- **T4** Verify power redundancy per rack.
- **T5** Verify the power capacity by PDU type.
- **T6** Describe CDUs for liquid-cooled racks.
- **T7** Verify grounding.
- **T8** Differentiate between hot-aisle and cold-aisle cooling.

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



## High-Density Cabling Installation for AI Clusters - 30%
This section details the practical deployment of high-density cables. It covers distinguishing between NVIDIA and other cables, understanding transceiver form factors (OSFP/QSFP) and fiber types (MMF/SMF), deploying InfiniBand copper and MPO/APC fiber optic cables, implementing the 50/50 left-right routing strategy, and applying professional cable management practices, including cleaning connectors.

### Potential Exam Topics:
- **T1** Describe the difference between NVIDIA cables vs. others.
- **T2** Describe the different transceiver form factors (OSFP vs. QSFP).
- **T3** Describe the difference between MMF and SMF.
- **T4** Describe the transceiver requirements across the various SMF distances.
- **T5** Deploy InfiniBand NDR/XDR copper cables.
- **T6** Install MPO/APC fiber optic cables.
- **T7** Implement 50/50 left-right cable routing strategy.
- **T8** Bundle and dress cables professionally (hook and loop fasteners, soft ties, color coding).
- **T9** Install fiber optic transceivers and clean connectors.

### Suggested Readings and Recommended Training for High-Density Cabling Installation

**SR1** Cable Validation Tool (CVT) Fundamentals: free self-paced course

**SR2** Choosing Between OSFP and QSFP-DD: Key Considerations for 800G Optical Transceivers
- [OSFP vs QSFP-DD for 800G, explained](2.SR2/osfp-vs-qsfpdd-explained.html)

**SR3** Cable Management Best Practices—NVIDIA DGX SuperPOD™
- [Cable management best practices, explained](2.SR3/cable-management-best-practices.html)

**SR4** Deploying the Bundles—NVIDIA DGX SuperPOD: Cabling Data Centers Design Guide
- [Deploying the bundles, explained](2.SR4/deploying-the-bundles-explained.html)

**SR5** Maintaining NDR Connectors and Cables—NVIDIA DGX SuperPOD
- [Keeping NDR optics clean](2.SR5/ndr-connector-maintenance-explained.html)

**SR6** Connectors and Cages
- [Connectors and cages, explained (NVIDIA LinkX)](2.SR6/nvidia-connectors-and-cages.html)

**SR7** Validated and Supported Cables and Switches—NVIDIA Docs
- [ConnectX-7 validated cables & switches, explained](2.SR7/connectx7-cables-explained.html)

**SR8** NVIDIA Q32xx and Q34xx XDR 800 Gb/s InfiniBand Switch Systems User Manual
- [Reading the LEDs on Q32xx / Q34xx XDR switches](2.SR8/nvidia-xdr-switch-led-guide.html)

**SR9** How to Understand OSFP vs. QSFP-DD Form Factors—BYXGD
- [OSFP vs QSFP-DD, explained visually](2.SR9/osfp-vs-qsfp-dd-explained.html)

**SR10** 200G Optical Transceiver: QSFP‑DD vs. OSFP for Data Centers
- [200G transceivers: QSFP-DD vs OSFP, explained](2.SR10/200g-qsfp-dd-vs-osfp-explained.html)

**SR11** Single Mode vs. Multimode Fiber: A Complete Comparison Guide
- [Single-mode vs multimode fiber, explained visually](2.SR11/single-mode-vs-multimode-fiber2.html)

**SR12** Single-Mode vs. Multimode Fiber: A Comprehensive Guide
- [Single-mode vs multimode fiber, explained](2.SR12/single-mode-vs-multimode-fiber.html)

**SR13** 2 Big Mistakes to Avoid During Fiber Cable Installation
- [Two big mistakes in fiber installation](2.SR13/fiber-installation-mistakes.html)

**SR14** Single-Mode vs. Multimode Fiber—DCD
- [Single-mode vs multimode fiber (DCD), explained](2.SR14/single-mode-vs-multimode-fiber3.html)

**SR15** Cleaning and Inspecting MPO/MTP Connectors | Fluke Networks
- [Cleaning and inspecting MPO/MTP connectors](2.SR15/mpo-mtp-cleaning-inspection.html)

**SR16** The Fiber Optic Association, Inc.
- [Fiber optic installation — FOA guide](2.SR16/foa-fiber-installation-explained.html)

**SR17** Installing an OSFP Transceiver
- [Installing an OSFP transceiver — visual guide](2.SR17/osfp-transceiver-install.html)

**SR18** Clean & Inspect: What IEC 61300-3-35 Means to You | MicroCare
- [Clean & inspect — IEC 61300-3-35 explained](2.SR18/iec-61300-3-35-explained.html)
