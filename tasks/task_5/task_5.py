import helpers


def task_5(mode="test"):
    """
    Goal:
        Create a realistic file where you insert the needles in a haystack
    Instructions:
        - Load the groundtruth from outputs/task_4_groundtruth.json
        - Insert the groundtruth_answers into a single text file to act as a knowledge base.
        - The file should be a single text file with the user query and the  groundtruth_answers.
        - The file should be saved to outputs/task_5_needle_in_haystack.txt
    """
    # Load the groundtruth JSON file
    groundtruth = helpers.load_json("tasks/task_4/task_4_groundtruth.json")
    
    user_query = groundtruth["user_query"]
    answers = groundtruth["groundtruth_answers"]
    
    # Create haystack text - a realistic knowledge base document with answers embedded
    haystack_content = f"""================================================================================
ENERGY MANAGEMENT KNOWLEDGE BASE
================================================================================

Document ID: KB-2024-ENERGY-001
Last Updated: December 2024
Category: Residential Energy Management

--------------------------------------------------------------------------------
SECTION 1: Introduction to Residential Energy Consumption
--------------------------------------------------------------------------------

Energy consumption in residential buildings has become a critical topic in modern 
sustainability discussions. As households continue to grow and technology becomes 
more integrated into daily life, understanding and managing energy use has never 
been more important.

The average household consumes approximately 10,500 kWh annually, with significant 
variations based on geographic location, climate, and lifestyle factors. Peak 
demand periods typically occur during morning hours (6-9 AM) and evening hours 
(5-9 PM) when most families are active at home.

--------------------------------------------------------------------------------
SECTION 2: Understanding Peak Energy Demand
--------------------------------------------------------------------------------

Peak energy demand refers to periods when electricity consumption reaches its 
highest levels across the grid. These peaks create challenges for utility 
providers and can lead to higher electricity rates for consumers.

Key factors contributing to peak demand include:
- Air conditioning and heating systems
- Cooking appliances during meal preparation
- Entertainment systems and lighting
- Electric vehicle charging

During summer months, air conditioning can account for up to 50% of a household's 
energy consumption, making it a primary target for demand reduction strategies.

--------------------------------------------------------------------------------
SECTION 3: Strategies for Reducing Evening Peak Consumption
--------------------------------------------------------------------------------

USER QUERY: {user_query}

The following strategies have been identified as effective approaches:

3.1 Load Shifting and Activity Scheduling

{answers[0]}. This simple behavioral change can significantly reduce strain on 
the electrical grid while potentially lowering energy bills through time-of-use 
rate structures.

3.2 Smart Climate Control

{answers[1]}. Modern smart thermostats can learn household patterns and optimize 
heating and cooling schedules automatically, making this strategy increasingly 
accessible to homeowners.

--------------------------------------------------------------------------------
SECTION 4: Technology Solutions for Energy Management
--------------------------------------------------------------------------------

The integration of smart home technology has revolutionized how households manage 
their energy consumption. From simple programmable outlets to comprehensive home 
energy management systems, technology offers multiple pathways to efficiency.

4.1 Appliance Efficiency

{answers[2]}. The ENERGY STAR program provides guidance on selecting appliances 
that meet strict efficiency criteria established by the EPA.

4.2 Smart Home Integration

{answers[3]}. These systems can integrate with utility demand response signals 
to automatically adjust device operation during peak periods.

--------------------------------------------------------------------------------
SECTION 5: Utility Programs and Incentives
--------------------------------------------------------------------------------

Many utility companies offer programs designed to encourage customers to reduce 
consumption during peak periods. These programs benefit both the utility and 
the consumer.

5.1 Demand Response Participation

{answers[4]}. These programs may include direct load control, where the utility 
can briefly cycle air conditioning units, or voluntary reduction requests with 
bill credits for participation.

5.2 Rebate Programs

Utilities frequently offer rebates for energy-efficient appliance purchases, 
smart thermostat installations, and home weatherization improvements. These 
incentives help offset the initial cost of efficiency upgrades.

--------------------------------------------------------------------------------
SECTION 6: Building Envelope Improvements
--------------------------------------------------------------------------------

The physical structure of a home plays a crucial role in energy efficiency. 
Proper insulation, air sealing, and window treatments can dramatically reduce 
the energy required to maintain comfortable temperatures.

6.1 Insulation and Air Sealing

{answers[5]}. A professional energy audit can identify specific areas where 
improvements would provide the greatest benefit.

6.2 Windows and Doors

Energy-efficient windows with low-E coatings and proper weather stripping 
around doors can reduce heat transfer and minimize drafts that force HVAC 
systems to work harder.

--------------------------------------------------------------------------------
SECTION 7: Monitoring and Continuous Improvement
--------------------------------------------------------------------------------

Effective energy management requires ongoing attention and adjustment. Regular 
monitoring of energy consumption patterns helps identify opportunities for 
further improvement and ensures that implemented strategies continue to deliver 
expected results.

Many utilities now provide detailed usage data through online portals or mobile 
apps, making it easier than ever for households to track their consumption and 
measure the impact of efficiency measures.

--------------------------------------------------------------------------------
DOCUMENT METADATA
--------------------------------------------------------------------------------

Keywords: energy efficiency, peak demand, residential, smart home, demand response
Related Documents: KB-2024-SOLAR-001, KB-2024-HVAC-001, KB-2024-SMART-001
Review Date: June 2025

================================================================================
END OF DOCUMENT
================================================================================
"""
    
    # Save the needle-in-haystack file
    helpers.save_txt(haystack_content, "outputs/task_5_needle_in_haystack.txt")
    
    print(f"\nUser Query: {user_query}")
    print(f"\nNumber of needles (answers) embedded: {len(answers)}")
    print("\nNeedle in haystack file created successfully!")
    
    return {"user_query": user_query, "num_answers": len(answers)}
