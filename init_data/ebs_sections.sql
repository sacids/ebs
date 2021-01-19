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
-- Data for Name: sections; Type: TABLE DATA; Schema: public; Owner: sacids
--

INSERT INTO public.sections (id, code, title, description) VALUES (1, 1, 'Policy and legislative framework for implementation of EBS', 'Policy and legislative framework for implementation of EBS');
INSERT INTO public.sections (id, code, title, description) VALUES (2, 2, 'Staffing capacity and training', 'Staffing capacity and training');
INSERT INTO public.sections (id, code, title, description) VALUES (3, 3, 'Implementation readiness', 'Implementation readiness');
INSERT INTO public.sections (id, code, title, description) VALUES (4, 4, 'Resources', 'Resources');
INSERT INTO public.sections (id, code, title, description) VALUES (5, 5, 'Information gathering, epidemic intelligence and reporting', 'Information gathering, epidemic intelligence and reporting');
INSERT INTO public.sections (id, code, title, description) VALUES (6, 6, 'General issues', 'General issues');


--
-- Name: sections_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sacids
--

SELECT pg_catalog.setval('public.sections_id_seq', 6, true);


--
-- PostgreSQL database dump complete
--

