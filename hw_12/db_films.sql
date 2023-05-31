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
-- Name: films; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.films (
    title text NOT NULL,
    duration_min integer NOT NULL,
    genre text NOT NULL
);


ALTER TABLE public.films OWNER TO postgres;

--
-- Name: films_duretion_min_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.films_duretion_min_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.films_duretion_min_seq OWNER TO postgres;

--
-- Name: films_duretion_min_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.films_duretion_min_seq OWNED BY public.films.duration_min;


--
-- Name: films duration_min; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.films ALTER COLUMN duration_min SET DEFAULT nextval('public.films_duretion_min_seq'::regclass);


--
-- Data for Name: films; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.films (title, duration_min, genre) FROM stdin;
Inrestellar	169	epic science fiction film
Fight Club	139	drama
Kingsman: The secret Service	130	spy action comedy
\.


--
-- Name: films_duretion_min_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.films_duretion_min_seq', 1, false);


--
-- PostgreSQL database dump complete
--

