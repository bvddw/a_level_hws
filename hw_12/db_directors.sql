--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: directors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.directors (
    name text NOT NULL,
    age integer NOT NULL,
    number_of_films integer NOT NULL
);


ALTER TABLE public.directors OWNER TO postgres;

--
-- Name: directors_age_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.directors_age_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.directors_age_seq OWNER TO postgres;

--
-- Name: directors_age_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.directors_age_seq OWNED BY public.directors.age;


--
-- Name: directors_number_of_films_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.directors_number_of_films_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.directors_number_of_films_seq OWNER TO postgres;

--
-- Name: directors_number_of_films_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.directors_number_of_films_seq OWNED BY public.directors.number_of_films;


--
-- Name: directors age; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.directors ALTER COLUMN age SET DEFAULT nextval('public.directors_age_seq'::regclass);


--
-- Name: directors number_of_films; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.directors ALTER COLUMN number_of_films SET DEFAULT nextval('public.directors_number_of_films_seq'::regclass);


--
-- Data for Name: directors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.directors (name, age, number_of_films) FROM stdin;
Steven Spielberg	76	34
Martin Scorsese	80	25
Quentin Tarantino	60	10
\.


--
-- Name: directors_age_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.directors_age_seq', 1, false);


--
-- Name: directors_number_of_films_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.directors_number_of_films_seq', 1, false);


--
-- PostgreSQL database dump complete
--

