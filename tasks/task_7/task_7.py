import helpers


def task_7():
    """
    Goal:
        Create Three Needle-in-Haystack files (two of them are distractor files, and one is the target file from task 5)
    Instructions:
        - Create two distractor files by loading the passage from the file outputs/task_5_needle_in_haystack.txt
        - Create one target file by loading the passage from the file outputs/task_5_needle_in_haystack.txt
        - only file 1 is the target file, the other two are distractor files
        - Save the three files to the outputs/task_7_file_1.txt, outputs/task_7_file_2.txt, and outputs/task_7_file_3.txt
    """
    # Load the original needle-in-haystack content (target file)
    target_content = helpers.load_txt("outputs/task_5_needle_in_haystack.txt")
    
    # File 1: TARGET - the original needle-in-haystack file with correct answers
    helpers.save_txt(target_content, "outputs/task_7_file_1.txt")
    
    # File 2: DISTRACTOR - similar structure but with different/misleading content
    distractor_2 = """================================================================================
ENERGY MANAGEMENT KNOWLEDGE BASE
================================================================================

Document ID: KB-2024-ENERGY-002
Last Updated: November 2024
Category: Commercial Energy Management

--------------------------------------------------------------------------------
SECTION 1: Introduction to Commercial Energy Consumption
--------------------------------------------------------------------------------

Energy consumption in commercial buildings differs significantly from residential 
patterns. Office buildings, retail spaces, and industrial facilities each have 
unique energy profiles that require specialized management approaches.

The average commercial building consumes approximately 22.5 kWh per square foot 
annually, with significant variations based on building type and operational hours.
Peak demand periods for commercial buildings typically occur during business hours 
(9 AM - 5 PM) when HVAC and lighting systems are at full capacity.

--------------------------------------------------------------------------------
SECTION 2: Understanding Commercial Peak Energy Demand
--------------------------------------------------------------------------------

Commercial peak energy demand is driven by different factors than residential 
consumption. Large HVAC systems, industrial equipment, and extensive lighting 
contribute to high baseline consumption.

Key factors contributing to commercial peak demand include:
- Central HVAC systems serving large floor areas
- Industrial machinery and production equipment
- Data center cooling requirements
- Commercial kitchen operations

During peak business hours, HVAC can account for up to 40% of a commercial 
building's energy consumption.

--------------------------------------------------------------------------------
SECTION 3: Strategies for Commercial Energy Reduction
--------------------------------------------------------------------------------

USER QUERY: How can commercial buildings optimize energy usage during business hours

The following strategies have been identified for commercial applications:

3.1 Building Automation Systems

Commercial buildings benefit from centralized building management systems that 
coordinate HVAC, lighting, and equipment schedules. These systems can respond 
to occupancy sensors and adjust consumption accordingly.

3.2 Demand-Controlled Ventilation

Installing CO2 sensors to control ventilation rates based on actual occupancy 
can reduce HVAC energy consumption by 10-30% in spaces with variable occupancy.

--------------------------------------------------------------------------------
SECTION 4: Industrial Energy Solutions
--------------------------------------------------------------------------------

Industrial facilities face unique challenges in managing energy consumption. 
Production schedules, equipment efficiency, and process optimization all play 
important roles in overall energy management.

4.1 Motor and Drive Efficiency

Variable frequency drives on motors can reduce energy consumption by matching 
motor speed to actual load requirements rather than running at full speed.

4.2 Process Heat Recovery

Capturing waste heat from industrial processes and using it for space heating 
or preheating can significantly reduce overall energy consumption.

--------------------------------------------------------------------------------
SECTION 5: Renewable Energy Integration
--------------------------------------------------------------------------------

Many commercial and industrial facilities are integrating on-site renewable 
energy generation to reduce grid dependence and lower operating costs.

5.1 Solar PV Systems

Rooftop and ground-mounted solar installations can offset significant portions 
of daytime energy consumption when properly sized for the facility.

5.2 Battery Storage Systems

Energy storage allows facilities to store excess renewable generation for use 
during peak demand periods or grid outages.

--------------------------------------------------------------------------------
SECTION 6: Energy Procurement Strategies
--------------------------------------------------------------------------------

Large energy consumers can benefit from strategic procurement practices that 
go beyond simple rate negotiations.

6.1 Power Purchase Agreements

Long-term contracts for renewable energy can provide price stability and 
support sustainability goals while potentially reducing overall energy costs.

6.2 Peak Demand Management Contracts

Negotiating contracts with demand charges in mind can lead to significant 
savings for facilities with high but brief peak demands.

--------------------------------------------------------------------------------
SECTION 7: Compliance and Reporting
--------------------------------------------------------------------------------

Commercial and industrial facilities often face regulatory requirements for 
energy reporting and efficiency improvements.

Building energy benchmarking programs require regular disclosure of energy 
performance metrics, creating incentives for continuous improvement.

--------------------------------------------------------------------------------
DOCUMENT METADATA
--------------------------------------------------------------------------------

Keywords: commercial energy, industrial efficiency, building automation, renewable
Related Documents: KB-2024-SOLAR-002, KB-2024-HVAC-002, KB-2024-INDUSTRIAL-001
Review Date: May 2025

================================================================================
END OF DOCUMENT
================================================================================
"""
    helpers.save_txt(distractor_2, "outputs/task_7_file_2.txt")
    
    # File 3: DISTRACTOR - another similar document with different focus
    distractor_3 = """================================================================================
ENERGY MANAGEMENT KNOWLEDGE BASE
================================================================================

Document ID: KB-2024-ENERGY-003
Last Updated: October 2024
Category: Renewable Energy Systems

--------------------------------------------------------------------------------
SECTION 1: Introduction to Home Renewable Energy
--------------------------------------------------------------------------------

Renewable energy adoption in residential settings has grown dramatically over 
the past decade. Solar panels, small wind turbines, and geothermal systems are 
becoming increasingly accessible to homeowners.

The average residential solar installation produces approximately 8,000 kWh 
annually, with significant variations based on geographic location, roof 
orientation, and system size. Production peaks typically occur during midday 
hours (10 AM - 2 PM) when solar irradiance is highest.

--------------------------------------------------------------------------------
SECTION 2: Understanding Solar Energy Production
--------------------------------------------------------------------------------

Solar energy production follows predictable patterns based on time of day, 
season, and weather conditions. Understanding these patterns is essential for 
maximizing the value of a solar installation.

Key factors affecting solar production include:
- Roof orientation and tilt angle
- Shading from trees or nearby structures
- Panel efficiency and degradation over time
- Inverter performance and capacity

During summer months, a well-designed system can produce 50% more energy than 
during winter months due to longer days and higher sun angles.

--------------------------------------------------------------------------------
SECTION 3: Strategies for Maximizing Solar Value
--------------------------------------------------------------------------------

USER QUERY: How can homeowners get the most value from their solar installation

The following strategies have been identified for solar optimization:

3.1 Self-Consumption Optimization

Running high-consumption appliances during peak solar production hours ensures 
that generated electricity is used on-site rather than exported to the grid 
at potentially lower rates.

3.2 Battery Storage Integration

Adding battery storage allows homeowners to store excess daytime production 
for use during evening hours when solar generation drops but consumption 
typically increases.

--------------------------------------------------------------------------------
SECTION 4: Grid Integration Considerations
--------------------------------------------------------------------------------

How solar installations interact with the utility grid affects both the 
economics and practicality of residential renewable energy systems.

4.1 Net Metering Policies

Understanding local net metering policies is essential for calculating the 
financial return on solar investment. Policies vary significantly by state 
and utility service territory.

4.2 Grid Connection Requirements

Utilities have specific requirements for grid-connected solar installations 
including equipment specifications, inspection processes, and interconnection 
agreements.

--------------------------------------------------------------------------------
SECTION 5: Alternative Renewable Technologies
--------------------------------------------------------------------------------

While solar is the most common residential renewable technology, other options 
may be suitable depending on site conditions and local resources.

5.1 Small Wind Systems

Properties with adequate wind resources and sufficient setback distances may 
benefit from small wind turbines as a complement to or alternative to solar.

5.2 Geothermal Heat Pumps

Ground-source heat pumps can significantly reduce heating and cooling energy 
consumption by leveraging stable underground temperatures for heat exchange.

--------------------------------------------------------------------------------
SECTION 6: Financial Considerations
--------------------------------------------------------------------------------

The economics of residential renewable energy depend on multiple factors 
including installation costs, available incentives, and local electricity rates.

6.1 Federal Tax Credits

The federal investment tax credit provides significant savings on qualifying 
solar and storage installations, reducing the net cost substantially.

6.2 State and Local Incentives

Additional incentives from state governments, utilities, and local programs 
can further improve the economics of renewable energy installations.

--------------------------------------------------------------------------------
SECTION 7: Maintenance and Monitoring
--------------------------------------------------------------------------------

Proper maintenance and monitoring ensure that renewable energy systems continue 
to perform optimally throughout their expected lifespan.

Regular monitoring of production data helps identify any performance issues 
early, allowing for prompt maintenance before significant production losses occur.

--------------------------------------------------------------------------------
DOCUMENT METADATA
--------------------------------------------------------------------------------

Keywords: solar energy, renewable, battery storage, net metering, clean energy
Related Documents: KB-2024-SOLAR-001, KB-2024-BATTERY-001, KB-2024-WIND-001
Review Date: April 2025

================================================================================
END OF DOCUMENT
================================================================================
"""
    helpers.save_txt(distractor_3, "outputs/task_7_file_3.txt")
    
    print("Created 3 needle-in-haystack files:")
    print("  - outputs/task_7_file_1.txt (TARGET - contains correct answers)")
    print("  - outputs/task_7_file_2.txt (DISTRACTOR - commercial energy focus)")
    print("  - outputs/task_7_file_3.txt (DISTRACTOR - renewable energy focus)")
    
    return {
        "target_file": "outputs/task_7_file_1.txt",
        "distractor_files": ["outputs/task_7_file_2.txt", "outputs/task_7_file_3.txt"]
    }
