--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4
-- Dumped by pg_dump version 12.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: question_lists; Type: TABLE DATA; Schema: public; Owner: sacids
--

INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (78, '1.6', 'Is there National Public Health Institute (NPHI) established in the country or a coordinating structure for the NPHI?', 'RADIO', 'NO', 6, '"It could be a fully-fledged institute, or could be some structure performing the duties of the NPHI. Describe what is available. "', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (82, '﻿2.1', 'Is there a National Public Health institute (NPHI) or a unit/department serving the functions of NPHI?', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (94, '2.3', 'What type of existing workforce are available to support the EBS roll out and conduct surveillance at various levels of service delivery? ', 'NONE', 'NO', 1, '"Where possible indicate what the guidelines prescribe and what is in place in terms of cadres, and highest qualifications of occupants at national, intermediate, health facility and community levels.  Provide information and evidence of  differences, if any, in deployment by geographical locations of the country"
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (95, '2.3.1', 'Medical doctors', 'NONE', 'NO', 1, '"Provide title and numbers of staff in the category and level of care (national, intermediate, health facility and community) and highest qualification"
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (96, '2.3.2', 'Nurses', 'NONE', 'NO', 1, '"Provide title and numbers of staff in the category and level of care (national, intermediate, health facility and community) and highest qualification"
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (97, '2.3.3', 'Public health officers', 'NONE', 'NO', 1, '"Provide title and numbers of staff in the category and level of care (national, intermediate, health facility and community) and highest qualification"
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (98, '2.3.4', 'Epidemiologists', 'NONE', 'NO', 1, '"Provide title and numbers of staff in the category and level of care (national, intermediate, health facility and community) and highest qualification"
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (99, '2.3.5', 'Laboratory technologists', 'NONE', 'NO', 1, '"Provide title and numbers of staff in the category and level of care (national, intermediate, health facility and community) and highest qualification"
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (100, '2.3.6', 'Animal health  specialists ', 'NONE', 'NO', 1, '"Provide title and numbers of staff in the category and level of care (national, intermediate, health facility and community) and highest qualification"
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (101, '2.3.7', 'Other cadres (specify) ', 'NONE', 'NO', 1, '"Provide title and numbers of staff in the category and level of care (national, intermediate, health facility and community) and highest qualification"
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (102, '2.4', 'How many staff at NPHI are trained to implement or roll out the EBS in the country', 'NONE', 'NO', 1, 'Indicate the specialized training for rolling out EBS they have received. Provide numbers and the training
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (103, '2.5', 'Are there  EBS focal points/persons identified at various levels of health care? ', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (179, '5.14', 'Are the units staffed with a trained workforce capable of analyzing and interpreting data in real time?', 'NONE', 'NO', 1, 'Indicate if it is available for 24/7', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (180, '5.15', 'Is there capacity and or capacity building at the lowest level of health system to be able to analyse and use data for decision making', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (181, '5.16', 'Is there a plan for monitoring and evaluation of EBS system?', 'NONE', 'NO', 1, '"Share the reporting framework and key performance indicators , if available"
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (182, '5.17', 'Is there a plan for conducting data quality assessment to verify events and implementation of the system ', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (74, '1.2', 'Has the government developed a guidance document for establishing EBS in the country?', 'RADIO', 'NO', 1, '"Guidance document may include national strategy, technical guidelines or any other document that provides instructions to health workers on what should be done to implement EBS at any level. Attach copies available."', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (75, '1.3', '"If yes to question 1.2, does the guidance document cover sectors beyond human health-related such as animal, agriculture, environment, customs, immigration etc ?"', 'RADIO', 'NO', 1, '"Do the documents propose routine collaboration and sharing of information, beyond just mentioning ""multi-sectoral"" . Do they require health to involve other sectors and vice versa in collecting data on potential acute health events"', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (83, '2.2', 'What is the level of staffing/number of staff at the NPHI?', 'NONE', 'NO', 1, 'Number under each category', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (76, '1.4', 'Has the government appointed a national focal person for EBS or an officer In-charge of EBS identified?', 'RADIO', 'NO', 4, 'Is there a dedicated official who''s responsible for EBS or early warning and response at national level. May be assigned the role in addition to other duties.', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (77, '1.5', 'Has the government developed a roll-out plan for EBS in the country?', 'RADIO', 'NO', 5, '"Provide evidence of a plan with activities and timelines', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (79, '1.7', '"Is there established Emergency Operating Center (EOC) in the country?  If No, go to question 1.9"', 'RADIO', 'NO', 7, '"Is there a PHEOC', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (80, '1.8', 'Does the EOC have the essential components to function effectively?', 'RADIO', 'NO', 8, 'Describe the status of: Availability and use of (i)written plans and procedures', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (84, '2.2.1', 'Director', 'NONE', 'NO', 1, 'This refers to head of NPHI. Could be known by other title. Indicate.', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (93, '2.2.11', 'Other staffing (specify)……………', 'NONE', 'NO', 2, 'Provide title and numbers of staff in the category and highest qualification', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (85, '2.2.3', 'Epidemiologists', 'NONE', 'NO', 3, 'Numbers of staff in the category and highest qualification', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (86, '2.2.4', 'Laboratory experts', 'NONE', 'NO', 4, 'Numbers of staff in the category and highest qualification', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (87, '2.2.5', 'Public health experts', 'NONE', 'NO', 5, 'Numbers of staff in the category and highest qualification', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (88, '2.2.6', 'Data analysts', 'NONE', 'NO', 6, 'Numbers of staff in the category and highest qualification', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (89, '2.2.7', 'Environmental health officers', 'NONE', 'NO', 7, 'Numbers of staff in the category and highest qualification', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (90, '2.2.8', 'Research Scientists', 'NONE', 'NO', 8, 'Numbers of staff in the category and highest qualification', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (91, '2.2.9', 'Animal health  specialists', 'NONE', 'NO', 9, 'Numbers of staff in the category and highest qualification', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (92, '2.2.10', 'Risk communication officer', 'NONE', 'NO', 2, 'Numbers of staff in the category and highest qualification', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (104, '2.6', 'Is there a training curriculum and plan for EBS in place?', 'NONE', 'NO', 1, 'Indicate the availability of curriculum and training plan for country-wide coverage. The plan should have stated activities and timelines. Attach if available.
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (105, '2.7', '"Has the country adopted and rolled out integregated disease surveilance and response (IDSR) strategy? If NO to 2.7, skip to question 2.9"', 'NONE', 'NO', 1, 'Indicate the version of the strategy currently under implementation/in the process of roll out in the country. 
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (106, '2.8', '"If rolled out, what is the national coverag of DSR roll out?  "', 'NONE', 'NO', 1, 'Indicate the levels and numbers of workers trained and the total that are not covered yet (to show the existing gap). Provide geographic reach of IDRS in the country.
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (107, '2.9', 'Has the country conducted any form of training on EBS?', 'NONE', 'NO', 1, 'This is to show the levels where the training has occurred and whether the trainees have been retained
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (108, '2.9.1', 'Training of trainers (TOT)', 'NONE', 'NO', 1, '"Indicate the numbers, location within the country (geographical) and level of care the trainees are currently serving "
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (109, '2.9.2', 'Frontline works', 'NONE', 'NO', 1, '"Indicate the numbers, location within the country (geographical) and level of care the trainees are currently serving "
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (110, '2.9.3', 'Community health workers/village health volunteers ', 'NONE', 'NO', 1, '"Indicate the numbers, location within the country (geographical) and level of care the trainees are currently serving "
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (111, '2.10', 'Are there nominated rapid response teams (RRT) in various regions/districts/counties?', 'NONE', 'NO', 1, '"To show whetehr Rapid Response Teams are available at national, and intermediate levels"
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (112, '2.11', 'What is the level of training currently undertaken on the RRT?', 'NONE', 'NO', 1, 'Indicate the coverage of RRT-specific training by the various of service delivery levels and location/regions covered', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (113, '﻿3.1', 'Does the government have a roll out plan for EBS? ', 'NONE', 'NO', 1, 'Provide a copy of the roll out plan. If under development provide details. Which sectors are involved?
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (114, '3.2', 'Has the MoH rolled out EBS at various levels of health care? ', 'NONE', 'NO', 1, 'Provide evidence of the plan', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (115, '3.3', '"If yes, what is the scope of interventions and structures for EBS in each level of service delivery?"', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (116, '3.3.1', 'National level ', 'NONE', 'NO', 1, '"Are the follwing processes in place: hotline, advocacy for EBS and use of hotline', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (117, '3.3.2', 'Sub-national/intermediate level (Regional/Province/County', 'NONE', 'NO', 1, ' District/sub-county)', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (118, '3.3.3', 'Health facilities', 'NONE', 'NO', 1, 'Comment on availability of HEBS Focal Points in all EBS implementing facilities? Are SOPs for reporting signals in place? 
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (119, '3.3.4', 'Community level ', 'NONE', 'NO', 1, 'Provide info on availability of community health volunteers and their training on EBS', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (120, '3.4', 'Have coordination mechanisms between various levels of government and across relevant collaborating sectors including integration and use of data at all levels been established?', 'NONE', 'NO', 1, 'Evidence of inter-sector data sharing schemes. Examples of inter-sectoral communication may be attached.
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (121, '3.5', '"Are other sectors beyond human health such as animal, agriculture, environment, customs, immigration, etc playing an active role in the EBS roll out? If None, skip to question 3.7"', 'NONE', 'NO', 1, '"If ""Yes"" provide evidence."
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (122, '3.6', '"If involved, at what levels are they involved (community, health facility, intermediate, national levels?"', 'NONE', 'NO', 1, 'Indicate the nature of collaboration at the various levels of EBS implementation
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (123, '3.7', 'Have the roles and responsibilities of various stakeholders at the various levels of health system involved in the implementation of EBS been clearly outlined. ', 'NONE', 'NO', 1, 'Provide roles and responsibilities/terms of reference of the various levels', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (124, '3.8', 'Are there technical working groups at various levels of service delivery with responsibility to roll out EBS? (the TWGs need not be specific but existing TWGs may have the added role of EBS implementation)', 'NONE', 'NO', 1, '"Provide evidence of meetings. Guidelines of their operation, if available."
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (125, '3.9', '"If yes, to 3.7 above, are these TWG multi-sectoral? (indicate the sectors represented)"', 'NONE', 'NO', 1, '"Indicate the sectors involved in EBS implementation at national. Intremediate, health facility and community levels"
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (126, '3.10', 'Has the country adopted/adapted the WHO AFRO IDSR technical guidelines (3rd edition of 2019). Explain which edition is currently in use', 'NONE', 'NO', 1, 'Provide a detailed list of priority diseases adopted by the country
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (127, '3.11', '"Has the country identied priority diseases for IDSR under the following categories (epidemic prone diseases, diseases targeted for eradication and elimination, diseases of public health importance including non-communicable diseases)"', 'NONE', 'NO', 1, 'Provide a detailed list of priority diseases adopted by the country. Highlight those that are not included in the WHO AFRO IDSR guidelines and reasons for their inclusion in the country one.
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (128, '3.12', 'Has the National TWG prepared and agreed upon a list of priority signals for EBS?', 'NONE', 'NO', 1, '"Provide a list of detailed signals for early detection, by level"
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (129, '3.13', 'Has the country developed signals that would allow for the early detection of events?', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (130, '3.13.1', 'Community level ', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (131, '3.13.2', 'Health facilities level ', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (135, '3.14', '"For communities, have the signals translated to local language where implementation has been prioritized?"', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (136, '3.15', 'Has field testing of the signals been done before roll out of the implementation of EBS?', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (137, '3.16', '"Has there been any level of engagement of community, "', 'NONE', 'NO', 1, 'Have communities been sensitized on EBS? What is the country coverage of such sensitization?
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (138, '3.17', '"If EBS in the country is not rolled out yet, what are the challenges?"', 'NONE', 'NO', 1, '', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (139, '﻿4.1', 'Is there an annual budget for the National Institute of Public Health/Country to discharge its functions?', 'NONE', 'NO', 1, '"Where the NHPI is not existent, is there a budget for that organ that coordinated EBS activities? Show evidence of the financial allocations"
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (183, '5.18', 'Please provide a snapshot of the performance based on the following selected indicators', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (184, '5.18.1', 'Proportion of rumour/signal investigated within 24 hours of reporting ', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (133, '3.13.4', 'Regional/Province/County level', 'NONE', 'NO', 1, '', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (134, '3.13.5', 'National  level', 'NONE', 'NO', 1, '', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (140, '4.2', '"Who are the financiers of the NPHI/Country Public Health functions (surveillance, preparedness and response etc)?"', 'NONE', 'NO', 1, 'Indicate the funding level - proportion of the total budget for EBS. Find status for at least the current and last financial years. Are there plans /promises for other funding sources.
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (141, '4.2.1', 'Government ', 'NONE', 'NO', 1, '(indicate the funding level - amount and proportion of the total budget)
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (142, '4.2.2', 'Regional organizations', 'NONE', 'NO', 1, '(indicate the funding level - amount and proportion of the total budget)
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (143, '4.2.3', 'Development Partners', 'NONE', 'NO', 1, '(indicate the funding level - amount and proportion of the total budget)
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (144, '4.2.4', 'Private sector ', 'NONE', 'NO', 1, '(indicate the funding level - amount and proportion of the total budget)
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (145, '4.2.5', 'Other sources (specify)', 'NONE', 'NO', 1, '(indicate the funding level - amount and proportion of the total budget)
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (146, '4.3', 'Is there a dedicated line item to implement EBS in the country budget?', 'NONE', 'NO', 1, 'What is the situation in the national and local governments where services and authority have been de-centralized
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (147, '4.4', 'Have the following resources been put in place to facilitate the implementation of EBS (this could be part of the ongoing surveillance planning) ', 'NONE', 'NO', 1, '"What is the status by level (national, intermediate, health facility and community)"
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (148, '4.4.1', '"EBS training manual for national, intermediate, health facility and community levels "', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (149, '4.4.2', 'EBS training curriculum/guidelines and associated resources to carry out training and refresher trainings', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (150, '4.4.3', 'Data collection tools for events and suspected outbreaks ', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (151, '4.4.4', 'Monitoring/supervision tools ', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (152, '4.4.5', 'Reporting tool to ensure rapid reporting from lower levels ', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (153, '4.4.6', '"Reporting tools such as cell phones, software such as District health information system "', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (154, '4.4.7', 'Budget for vehicle running to conduct verification and/or investigation ', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (155, '4.4.8', '"ICT equipment (Computers, printers, communication equipment etc) "', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (156, '4.5', ' Has there been support obtained from the RCC to facilitate EBS roll out in the country', 'NONE', 'NO', 1, '"State if there is any arrangement in pipeline, and if assistance may have covered other parts of the country and not others."
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (160, '4.6', 'Are there training physical facilities at the National Institute of Public Health that are available for training surveillance teams including EBS teams?', 'NONE', 'NO', 1, 'If not what are the alternative systems for training in place
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (161, '4.7', '"Are there virtual training facilities at the NPHI and other levels of service delivery, video conference facilities, eLearning Platforms and other virtual platforms"', 'NONE', 'NO', 1, 'Indicate the training resources available at national level. Indicate arrangements for training at lower levels in the country.
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (162, '4.8', 'Are the funding needs for EBS roll out met for the current year? ', 'NONE', 'NO', 1, '"Is there any support expected, but still in pipeline? What is the source?"
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (163, '4.9', 'If not what is the financial gap? ', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (164, '4.10', 'What are the areas/or components of EBS that are left uncovered or under funded?', 'NONE', 'NO', 1, 'Indicate the areas in the plan that are unfunded/underfunded. Find out the situation at national and lower levels
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (165, '4.11', 'Is there a resource mobilization strategy to finance EBS activities?', 'NONE', 'NO', 1, 'Both for national and lower levels', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (166, '﻿5.1', 'Have various potential sources of EBS data been mapped out/identified?', 'NONE', 'NO', 1, 'Both at National and lower levels
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (167, '5.2', 'Has there been a  system to capture and register  health events ', 'NONE', 'NO', 1, '"Provide details of the system', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (168, '5.3', 'Is there an SoP to standardise reporting and information flow for EBS reporting and feedback aligned with national surveillance and reporting structures? ', 'NONE', 'NO', 1, 'Could be part of the national guidelines. Attach if available.
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (169, '5.4', 'Are tools available for reporting and feedback at various levels  ', 'NONE', 'NO', 1, 'Existing tools for surveillance may be used and expanded to report events 
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (170, '5.5', '"If available, are the reporting tools electronic-based? "', 'NONE', 'NO', 1, 'Indicate the available tools at various levels s
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (171, '5.6', 'Are communication materials available e.g. posters? ', 'NONE', 'NO', 1, 'Provide copies if available
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (172, '5.7', '"Is there a mechanism in place for rapid reporting (phone, hotline, SMS based or social media platforms) "', 'NONE', 'NO', 1, 'indicate the various platforms available for reporting and feedback 
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (173, '5.8', 'What is the mobile phone network coverage in the country?', 'NONE', 'NO', 1, 'Indicate the proportion of mobile network coverage in various regions of the country 
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (174, '5.9', 'What is the level of mobile access and ownership by community members?', 'NONE', 'NO', 1, 'Indicate the mobile phone ownership level in the country (coverage with mobile phones by community)', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (175, '﻿5.10', '"If such mechasm exist, is there a team that is responsible for moderating the reports and immediately respond to the calls or requests of information on public health events from the community (call centre)"', 'NONE', 'NO', 1, 'This team could be part of the PHOEC. Indicate if such a team is at national level or at various levels of service delivery 
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (176, '5.11', '"Is there a designated unit at the national-level (e.g PHOEC) available to collect, collate, and analyze information collected through each type of EBS, or from the designated reporting modalities. If No, skip to question 5.15"', 'NONE', 'NO', 1, 'Indicate how the unit receives early warning and response information from the various levels of the health system.
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (177, '5.12', '"If such a unit exist, in which department/division of the Ministry is it hosted? "', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (178, '5.13', '"Does the unit routinely  analyze, and visualize data from both regular surveilance (indicator based) and EBS sources?"', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (158, '4.5.2', 'ii.     Materials, supplies and reagents (incl. PPE etc)', 'NONE', 'NO', 1, '', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (157, '4.5.1', 'i.     Field teams (travel costs)', 'NONE', 'NO', 1, '', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (159, '4.5.3', 'iii.     Communication and logistics (printing, transport etc)"', 'NONE', 'NO', 1, '', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (185, '5.18.2', 'Proportion of people from the community/village with immediate reportable symptoms and signs that attended the attached/nearby health facility in a week ', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (186, '5.18.3', 'Proportion of true events of public health importance detected (total number of true events detected) ', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (187, '5.18.4', 'Proportion of attended referrals with symptoms and signs that matched facility standard case definitions (SCD) and reported through e-IDSR ', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (188, '5.18.5', 'Proportion of rumours/signals reported by community health workers ', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (189, '5.18.6', 'Availability and use of rumour registers at the community/village level ', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (190, '5.18.7', 'Proportion of rumours/signals that were investigated by health facilities ', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (191, '5.18.8', 'Proportion of rumours/signals that were true events of public health importance ', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (192, '5.18.9', 'Proportion of expected monthly reports received at each level of reporting ', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (193, '5.18.10', 'Proportion of people from the community/village with immediate reportable symptoms and signs that attended the attached/nearby health facility in a week ', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (194, '5.18.11', '"Availability, use, and storage of referral forms at community and health facility "', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (195, '5.18.12', 'Proportion of attended referrals with symptoms and signs that matched facility SCD and reported through e-IDSR ', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (196, '5.18.13', '"Availability and use of community/facility SCDs, rumour register to monitor compiled information on referrals with symptoms and signs that matched facility SCD and reported through e-IDSR"', 'NONE', 'NO', 1, '', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (197, '﻿6.1', ' Which areas would you like to be supported to effectively roll out the implementation of the EBS in the Country?   ', 'NONE', 'NO', 1, '
', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (132, '3.13.3', 'Intermediate levels (District,/Sub-county) level', 'NONE', 'NO', 1, 'None', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (198, '6.1.1', 'Development of EBS strategy', 'NONE', 'NO', 1, '', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (199, '6.1.2', 'Development of roll out plan', 'NONE', 'NO', 1, '', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (200, '6.1.3', 'Training of TOTs for front-line health workers', 'NONE', 'NO', 1, '', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (201, '6.1.4', 'Step-down training', 'NONE', 'NO', 1, '', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (202, '6.1.6', 'Community level training', 'NONE', 'NO', 1, '', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (203, '6.1.7', 'Development of signals and priority events', 'NONE', 'NO', 1, '', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (204, '6.1.8', 'Others (list)', 'NONE', 'NO', 1, '', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (81, '1.9', 'Is there a established community structures for community based surveillance and community EBS (community health workers/volunteers structures in health care)?', 'RADIO', 'NO', 9, 'Evidence of policy/strategy/ for deploying cadres for detecting potential threats at community level. It is possible to have the function conducted without it being called EBS. Find out if there are community structures for detecting acute health events. Attach what is available.', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (73, '1.1', 'Is there a legal or policy framework for establishing event-based surveillance (EBS) system in the country?', 'RADIO', 'NO', 1, 'Providet evidence of any policy document providing for implementation of disease surveillance for early warning purposes in the country. May include adoption of the IDSR strategy in the country. Ask if statute declaration is available or in the making. Atach mentioned copies if available.', 'YES');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (205, '2.2.1.1', 'Phd', 'NUMBER', 'NO', 1, '', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (206, '2.2.1.2', 'Masters', 'NUMBER', 'NO', 2, '', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (207, '2.2.1.3', 'Bachelor Degree', 'NUMBER', 'NO', 3, '', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (208, '2.2.1.4', 'Diploma', 'NUMBER', 'NO', 4, '', 'NO');
INSERT INTO public.question_lists (id, code, title, qn_type, required, sort_order, hints, has_upload) VALUES (209, '2.2.1.5', 'Certicate', 'NUMBER', 'NO', 5, '', 'NO');


--
-- Name: question_lists_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sacids
--

SELECT pg_catalog.setval('public.question_lists_id_seq', 209, true);


--
-- PostgreSQL database dump complete
--

