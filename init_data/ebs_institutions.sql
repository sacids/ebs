--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4 (Ubuntu 12.4-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.4 (Ubuntu 12.4-0ubuntu0.20.04.1)

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
-- Data for Name: institutions; Type: TABLE DATA; Schema: public; Owner: sacids
--

INSERT INTO public.institutions (id, title, initial, description, logo, country_id) VALUES (2, 'Sacids Foundation For One Health', 'SACIDS', 'The SACIDS Foundation for One Health (SACIDS) is a ONE HEALTH Virtual Institute that links academic and research institutions in Southern and East Africa, which deal with infectious diseases of humans and animals within the African Ecosystem, in an innovative South-South-North smart partnership with world-renowned centres of research and training.', 'photos/sacids_Q8R9pYw.jpeg', 10);
INSERT INTO public.institutions (id, title, initial, description, logo, country_id) VALUES (3, 'East, Central and Southern African Health Community (ECSA-HC)', 'ECSA', 'The East, Central and Southern African Health Community (ECSA-HC) is an inter-governmental health organization that fosters and promotes regional cooperation in health among member states. Member states of the ECSA Health Community are Kenya, Lesotho, Malawi, Mauritius, Eswatini, United Republic of Tanzania, Uganda, Zambia and Zimbabwe.', 'photos/ecsa-logo.png', 10);
INSERT INTO public.institutions (id, title, initial, description, logo, country_id) VALUES (4, 'Africa CDC', 'Africa CDC', 'Africa CDC strengthens the capacity and capability of Africa’s public health institutions as well as partnerships to detect and respond quickly and effectively to disease threats and outbreaks, based on data-driven interventions and programmes.', 'photos/africacdc.png', 10);


--
-- Name: institutions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sacids
--

SELECT pg_catalog.setval('public.institutions_id_seq', 4, true);


--
-- PostgreSQL database dump complete
--

