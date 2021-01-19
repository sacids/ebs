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
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: sacids
--

INSERT INTO public.categories (id, title, description, code) VALUES (6, 'General issues', 'None', 6);
INSERT INTO public.categories (id, title, description, code) VALUES (1, 'Policy and legislative framework for implementation of EBS', 'None', 1);
INSERT INTO public.categories (id, title, description, code) VALUES (2, 'Staffing capacity and training', 'None', 2);
INSERT INTO public.categories (id, title, description, code) VALUES (3, 'Implementation readiness', 'None', 3);
INSERT INTO public.categories (id, title, description, code) VALUES (4, 'Resources', 'None', 4);
INSERT INTO public.categories (id, title, description, code) VALUES (5, 'Information gathering, epidemic intelligence and reporting', 'None', 5);


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sacids
--

SELECT pg_catalog.setval('public.categories_id_seq', 6, true);


--
-- PostgreSQL database dump complete
--

