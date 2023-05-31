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
-- Name: actors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actors (
    name text NOT NULL,
    age integer NOT NULL,
    amount_of_films integer NOT NULL
);


ALTER TABLE public.actors OWNER TO postgres;

--
-- Name: actors_age_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.actors_age_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_age_seq OWNER TO postgres;

--
-- Name: actors_age_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.actors_age_seq OWNED BY public.actors.age;


--
-- Name: actors_amount_of_films_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.actors_amount_of_films_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_amount_of_films_seq OWNER TO postgres;

--
-- Name: actors_amount_of_films_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.actors_amount_of_films_seq OWNED BY public.actors.amount_of_films;


--
-- Name: actors age; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors ALTER COLUMN age SET DEFAULT nextval('public.actors_age_seq'::regclass);


--
-- Name: actors amount_of_films; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors ALTER COLUMN amount_of_films SET DEFAULT nextval('public.actors_amount_of_films_seq'::regclass);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actors (name, age, amount_of_films) FROM stdin;
Robert Downey Jr.	58	68
Johnny Depp	59	100
Leonardo DiCaprio	48	29
\.


--
-- Name: actors_age_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.actors_age_seq', 1, false);


--
-- Name: actors_amount_of_films_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.actors_amount_of_films_seq', 1, false);


--
-- PostgreSQL database dump complete
--

