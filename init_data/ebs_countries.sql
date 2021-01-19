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
-- Data for Name: contries; Type: TABLE DATA; Schema: public; Owner: sacids
--

INSERT INTO public.contries (id, title, council_id) VALUES (4, 'Kenya', 1);
INSERT INTO public.contries (id, title, council_id) VALUES (5, 'Eritrea', 1);
INSERT INTO public.contries (id, title, council_id) VALUES (6, 'Mauritius', 1);
INSERT INTO public.contries (id, title, council_id) VALUES (7, 'Rwanda', 1);
INSERT INTO public.contries (id, title, council_id) VALUES (8, 'Somalia', 1);
INSERT INTO public.contries (id, title, council_id) VALUES (9, 'Sudan', 1);
INSERT INTO public.contries (id, title, council_id) VALUES (10, 'Tanzania', 1);
INSERT INTO public.contries (id, title, council_id) VALUES (11, 'Uganda', 1);
INSERT INTO public.contries (id, title, council_id) VALUES (12, 'Sao Tomé and Principe', 1);
INSERT INTO public.contries (id, title, council_id) VALUES (13, 'Comoros', 2);
INSERT INTO public.contries (id, title, council_id) VALUES (14, 'Djibouti', 2);
INSERT INTO public.contries (id, title, council_id) VALUES (15, 'Madagascar', 2);
INSERT INTO public.contries (id, title, council_id) VALUES (16, 'Burundi', 2);
INSERT INTO public.contries (id, title, council_id) VALUES (17, 'Cameroon', 2);
INSERT INTO public.contries (id, title, council_id) VALUES (18, 'Republic of Central Africa', 2);
INSERT INTO public.contries (id, title, council_id) VALUES (19, 'Tchad', 2);
INSERT INTO public.contries (id, title, council_id) VALUES (20, 'Republic of Democratic Republic of Congo', 2);
INSERT INTO public.contries (id, title, council_id) VALUES (21, 'Guinea Equatorial', 2);
INSERT INTO public.contries (id, title, council_id) VALUES (22, 'Gabon', 2);
INSERT INTO public.contries (id, title, council_id) VALUES (23, 'Ethiopia', 3);


--
-- Name: contries_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sacids
--

SELECT pg_catalog.setval('public.contries_id_seq', 23, true);


--
-- PostgreSQL database dump complete
--

