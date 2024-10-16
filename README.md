# MapReduce with Python

Find a few answers from a large dataset.

## Description

The quest is simple. Use MapReduce algortihm to find the answer for the following questions.

1. Find the # of flights each airline made so far  from 1987 until recent.
2. Find the mean departure delay per origination airport.
3. What day the delays are the worst?

## Hints

MapReduce algorithm is designed to be seperated. Use this to your advantage. 

1. Make 3 functions: `Mapper`, `Sorter`, `Reducer`.
2. Use threading or multiprocessing while you are mapping or sorting different files.
3. For things you multiprocessed, write down the results into temporary files.
4. Use `functools.reduce`, `itertools.groupby` and builtin `map` function.

## Dataset

You will be working on `Airline On-Time Performance Dataset`. Dataset is availabe at my Google Drive. Use your **school ID** to access to the [folder](https://drive.google.com/drive/folders/1145wIkSlzA61CdHS4hZZFgF6ZzIbaVJM?usp=sharing). 

The data consists of flight arrival and departure details for all commercial flights within the USA, from October 1987 to April 2008. It has a total file size of 1.6 GB (compressed, and 12 GB when uncompressed), with the number of records a little over 123 million records.

Each row represents an individual flight record with details of that flight in the row. The information are:

| No  | Name              | Data Type | Description                                                               |
| --- | ----------------- | --------- | ------------------------------------------------------------------------- |
| 1   | Year              | int64     | 1987-2008                                                                 |
| 2   | Month             | int64     | 1-12                                                                      |
| 3   | DayofMonth        | int64     | 1-31                                                                      |
| 4   | DayOfWeek         | int64     | 1 (Monday) - 7 (Sunday)                                                   |
| 5   | DepTime           | float64   | actual departure time (local, hhmm)                                       |
| 6   | CRSDepTime        | float64   | scheduled departure time (local, hhmm)                                    |
| 7   | ArrTime           | float64   | actual arrival time (local, hhmm)                                         |
| 8   | CRSArrTime        | float64   | scheduled arrival time (local, hhmm)                                      |
| 9   | UniqueCarrier     | string    | unique carrier code                                                       |
| 10  | FlightNum         | float64   | flight number                                                             |
| 11  | TailNum           | string    | plane tail number                                                         |
| 12  | ActualElapsedTime | float64   | in minutes                                                                |
| 13  | CRSElapsedTime    | float64   | in minutes                                                                |
| 14  | AirTime           | float64   | in minutes                                                                |
| 15  | ArrDelay          | float64   | arrival delay, in minutes                                                 |
| 16  | DepDelay          | float64   | departure delay, in minutes                                               |
| 17  | Origin            | string    | origin IATA airport code                                                  |
| 18  | Dest              | string    | destination IATA airport code                                             |
| 19  | Distance          | float64   | in miles                                                                  |
| 20  | TaxiIn            | float64   | taxi in time, in minutes                                                  |
| 21  | TaxiOut           | float64   | taxi out time in minutes                                                  |
| 22  | Cancelled         | int64     | was the flight cancelled?                                                 |
| 23  | CancellationCode  | string    | reason for cancellation (A = carrier, B = weather, C = NAS, D = security) |
| 24  | Diverted          | int64     | 1 = yes, 0 = no                                                           |
| 25  | CarrierDelay      | float64   | in minutes                                                                |
| 26  | WeatherDelay      | float64   | in minutes                                                                |
| 27  | NASDelay          | float64   | in minutes                                                                |
| 28  | SecurityDelay     | float64   | in minutes                                                                |
| 29  | LateAircraftDelay | float64   | in minutes                                                                |

You can find more information about this dataset in the website of [Statistical Computing](http://stat-computing.org/dataexpo/2009/). Find out more information on [Airline On-Time Performance Data](https://www.transtats.bts.gov/DatabaseInfo.asp?QO_VQ=EFD&QO_anzr=Nv4yv0r%20b0-gvzr%20cr4s14zn0pr%20Qn6n) from [Bureau of Transportation Statistics (BTS)](https://www.transtats.bts.gov/).

## How to work on this Assignment?

1. Download this repository with [`git clone`](https://git-scm.com/docs/git-clone).
2. [Create a virtual environment](https://github.com/metinsenturk/class-materials/tree/main/contents/create-virtual-environment) and activate this environment everytime you need to use it.
3. Install [requirements.txt](requirements.txt) file using `pip install -r requirements.txt`.
4. Run the notebook.

## Questions

The repository should be self descriptive and it should guide you through assignment. Let me know if you have any questions.


----------
1-

Throughout 2024, I have been highly adaptable and committed to advancing my contributions to the organization's cybersecurity infrastructure. When a significant gap arose after the departure of the principal Splunk engineer, I stepped into the role seamlessly, wearing multiple hats and managing a diverse suite of critical security tools. This proactive shift demonstrates my commitment to *Ownership* and my ability to *Deliver Results* under high-pressure conditions, ensuring the continuity of mission-critical operations.

During this transition, I not only maintained our Splunk environment by optimizing resource allocation, patching, and scaling, but I also expanded our capabilities by integrating advanced telemetry solutions from Contrast Security, Snowflake, and Microsoft Sentinel SIEM. These efforts reflect a deep commitment to *Customer Obsession*, as I proactively addressed evolving security needs to strengthen our overall defensive posture.

In taking on the additional responsibilities of ExaBeam UBA use-case development and CrowdStrike administration, I demonstrated a *Bias for Action* by streamlining processes and ensuring that our security architecture remains resilient and scalable. These initiatives have not only improved our threat detection capabilities but also enhanced compliance and governance, creating a more robust security ecosystem for the business.

My ongoing pursuit of certifications, including the CCFA, CCFR, and Splunk Core User credentials, is further evidence of my commitment to *Learning and Being Curious*. By continuously investing in both my professional development and my academic journey as a PhD candidate in Artificial Intelligence and Decision Networks, I ensure that I remain at the forefront of technological advancements and bring cutting-edge insights back into our security framework.

Moreover, stepping into the Lead Analyst role during times of team shortages allowed me to further demonstrate *Insisting on the Highest Standards*. By triaging and investigating critical security incidents with precision, I ensured swift resolutions while maintaining detailed documentation that has become a key knowledge resource within the organization. My ability to *Earn Trust* through clear communication and my contributions to building a culture of continuous improvement are evident in the respect and recognition I’ve garnered from both leadership and peers.

Looking ahead, I remain focused on *Thinking Big* by driving strategic initiatives that align with our long-term goals, scaling our security infrastructure, and ensuring operational excellence. My role has continuously expanded to cover broader responsibilities, and I look forward to continuing to deliver high-impact outcomes that benefit both our customers and the organization as a whole.
----
2- 
Throughout 2024, I’ve remained committed to embracing and advancing the company’s Principles, ensuring that the work I deliver reflects the highest standards. Stepping into new roles and taking on expanded responsibilities in security engineering, I’ve prioritized not only technical excellence but also the well-being and growth of the team. This commitment is deeply tied to the Corporate Belonging and Inclusion initiative, where I’ve actively mentored peers, shared knowledge openly, and fostered a sense of collaboration across teams. My focus has always been on ensuring that both the team and our security infrastructure continue to evolve, making us stronger and more resilient, while creating an inclusive environment where everyone can contribute meaningfully.

------
  This year, I have been deeply involved in strengthening our risk management framework, prioritizing a proactive approach to identifying vulnerabilities and aligning our operations with compliance standards. With the departure of key personnel, I quickly took charge of critical security functions, ensuring seamless continuity and robust control over risk-sensitive areas. By closely monitoring risk indicators and implementing preventive measures across our security tools, I upheld a culture of accountability that directly supports our organizational objectives.
A key area where I have embodied risk culture is through the holistic management of our Splunk environment and associated telemetry tools like CrowdStrike, ExaBeam, and Microsoft Sentinel. My ability to promptly escalate potential security risks and implement timely solutions has been a cornerstone of my contributions, ensuring that no gaps were left unaddressed in our risk management processes. This involved continuously updating compliance requirements and integrating effective controls to align with regulatory frameworks and audit requirements. Additionally, I have contributed to creating a culture of open dialogue and transparency, encouraging team members to raise risk-related concerns, thus aligning with the company’s Three Lines of Defense strategy.

My work extends beyond just compliance, as I have been instrumental in documenting processes and developing best practices that are shared across the team, driving a collective understanding of risk ownership. This not only reinforces accountability but also ensures that we are equipped to respond to audit and regulatory inquiries with accuracy and efficiency. These actions have resulted in improved team competency around risk control and governance, while demonstrating my personal commitment to a strong risk culture.
