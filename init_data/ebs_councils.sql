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
-- Data for Name: councils; Type: TABLE DATA; Schema: public; Owner: sacids
--

INSERT INTO public.councils (id, title, description) VALUES (1, 'Eastern', 'Eastern');
INSERT INTO public.councils (id, title, description) VALUES (2, 'Central', 'Central');
INSERT INTO public.councils (id, title, description) VALUES (3, 'Ethiopia', 'Ethiopia');


--
-- Name: councils_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sacids
--

SELECT pg_catalog.setval('public.councils_id_seq', 3, true);


--
-- PostgreSQL database dump complete
--

