--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

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
    id integer NOT NULL,
    name character varying(50) DEFAULT 'N/A'::character varying NOT NULL,
    surname_first character varying(50) DEFAULT 'N/A'::character varying NOT NULL,
    surname_second character varying(50) DEFAULT 'N/A'::character varying NOT NULL
);


ALTER TABLE public.actors OWNER TO postgres;

--
-- Name: actors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.actors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_id_seq OWNER TO postgres;

--
-- Name: actors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.actors_id_seq OWNED BY public.actors.id;


--
-- Name: casting; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.casting (
    id_film integer,
    actor_1 integer,
    actor_2 integer,
    actor_3 integer,
    actor_4 integer,
    actor_5 integer,
    actor_6 integer,
    actor_7 integer
);


ALTER TABLE public.casting OWNER TO postgres;

--
-- Name: directors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.directors (
    id integer NOT NULL,
    name character varying(50),
    surname character varying(50)
);


ALTER TABLE public.directors OWNER TO postgres;

--
-- Name: directors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.directors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.directors_id_seq OWNER TO postgres;

--
-- Name: directors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.directors_id_seq OWNED BY public.directors.id;


--
-- Name: film_name; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.film_name (
    id integer NOT NULL,
    name_of_film character varying(100)
);


ALTER TABLE public.film_name OWNER TO postgres;

--
-- Name: film_name_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.film_name_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.film_name_id_seq OWNER TO postgres;

--
-- Name: film_name_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.film_name_id_seq OWNED BY public.film_name.id;


--
-- Name: films; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.films (
    id integer NOT NULL,
    name_of_film integer NOT NULL,
    director integer NOT NULL,
    year integer,
    cast_film integer
);


ALTER TABLE public.films OWNER TO postgres;

--
-- Name: films_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.films_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.films_id_seq OWNER TO postgres;

--
-- Name: films_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.films_id_seq OWNED BY public.films.id;


--
-- Name: actors id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors ALTER COLUMN id SET DEFAULT nextval('public.actors_id_seq'::regclass);


--
-- Name: directors id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.directors ALTER COLUMN id SET DEFAULT nextval('public.directors_id_seq'::regclass);


--
-- Name: film_name id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.film_name ALTER COLUMN id SET DEFAULT nextval('public.film_name_id_seq'::regclass);


--
-- Name: films id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.films ALTER COLUMN id SET DEFAULT nextval('public.films_id_seq'::regclass);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actors (id, name, surname_first, surname_second) FROM stdin;
1	Ben	Kingsley	N/A
2	Bonnie	Hunt	N/A
3	Caroline	Goodall	N/A
4	Clancy	Brown	N/A
5	Danny	Aiello	N/A
6	David	Morse	N/A
7	Dileep	Rao	N/A
8	Ellen	Page	N/A
9	Embeth	Davidz	N/A
10	Gary	Oldman	N/A
11	Gary	Sinise	N/A
12	Gil	Bellows	N/A
13	Hanna	R.Hall	N/A
14	James	Cromwell	N/A
15	Jean	Reno	N/A
16	Jonathan	Sagall	N/A
18	Ken	Watanabe	N/A
19	Leonardo	DiCaprio	N/A
20	Liam	Neeson	N/A
21	Mark	Rolson	N/A
17	Joseph	Gordon	Levitt
22	Michael	Clarke	Duncan
23	Michael	Conner	Humphreys
24	Michael	Jeter	N/A
25	Morgan	Freeman	N/A
26	Mykelti	Williamson	N/A
27	Natalie	Portman	N/A
28	Peter	Appel	N/A
29	Ralph	Fieness	N/A
30	Robin	Wright	N/A
31	Sally	Field	N/A
32	Tim	Robins	N/A
33	Tom	Hanks	N/A
34	Tom	Hardy	N/A
35	Willi	One	Blood
36	William	Sadler	N/A
37	Christian	Bale	N/A
38	Heath	Ledger	N/A
39	Aaron	Eckhart	N/A
40	Maggie	Gyllenhaal	N/A
41	Michael	Caine	N/A
42	Bruce	Willis	N/A
43	Milla	Jovovich	N/A
44	Ian	Holm	N/A
45	Chris	Tucker	N/A
46	Brion	James	N/A
47	Christopher	Walken	N/A
48	Martin	Sheen	N/A
49	Nathalie	Baye	N/A
50	Amy	Adams	N/A
51	Tom	Sizemore	N/A
52	Edward	Burns	N/A
53	Barry	Pepper	N/A
54	Adam	Goldberg	N/A
55	Vin	Diesel	N/A
\.


--
-- Data for Name: casting; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.casting (id_film, actor_1, actor_2, actor_3, actor_4, actor_5, actor_6, actor_7) FROM stdin;
1	33	30	31	11	26	23	13
2	19	17	8	34	18	7	\N
3	15	10	27	5	28	35	\N
4	20	1	29	3	9	16	\N
5	33	6	2	22	14	24	\N
6	32	25	36	4	12	21	\N
7	36	37	38	39	10	40	\N
8	42	43	10	44	45	46	\N
9	19	33	47	48	49	50	\N
10	33	51	52	53	54	55	\N
\.


--
-- Data for Name: directors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.directors (id, name, surname) FROM stdin;
1	Christopher	Nolan
2	Frank	Darabont
3	Luc	Besson
4	Robert	Zemeckis
5	Steven	Spilberg
\.


--
-- Data for Name: film_name; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.film_name (id, name_of_film) FROM stdin;
1	Forrest Gump
2	Inception
3	Leon
4	Schindler List
5	The Green Mile
6	The Shawshank Redemption
7	The Dark Knight
8	The Fifth Element
9	Catch Me If You Can
10	Saving Private Ryan
\.


--
-- Data for Name: films; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.films (id, name_of_film, director, year, cast_film) FROM stdin;
1	6	2	1994	6
2	5	2	1999	5
3	1	4	1994	1
4	4	5	1993	4
5	2	1	2010	2
6	3	3	1994	3
7	7	1	1994	7
8	8	3	1994	8
9	9	5	2002	9
10	10	5	1998	10
\.


--
-- Name: actors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.actors_id_seq', 55, true);


--
-- Name: directors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.directors_id_seq', 5, true);


--
-- Name: film_name_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.film_name_id_seq', 10, true);


--
-- Name: films_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.films_id_seq', 10, true);


--
-- Name: actors actors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (id);


--
-- Name: directors directors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.directors
    ADD CONSTRAINT directors_pkey PRIMARY KEY (id);


--
-- Name: film_name film_name_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.film_name
    ADD CONSTRAINT film_name_pkey PRIMARY KEY (id);


--
-- Name: films films_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.films
    ADD CONSTRAINT films_pkey PRIMARY KEY (id);


--
-- Name: casting casting2_actor_1_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.casting
    ADD CONSTRAINT casting2_actor_1_fkey FOREIGN KEY (actor_1) REFERENCES public.actors(id);


--
-- Name: casting casting2_actor_2_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.casting
    ADD CONSTRAINT casting2_actor_2_fkey FOREIGN KEY (actor_2) REFERENCES public.actors(id);


--
-- Name: casting casting2_actor_3_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.casting
    ADD CONSTRAINT casting2_actor_3_fkey FOREIGN KEY (actor_3) REFERENCES public.actors(id);


--
-- Name: casting casting2_actor_4_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.casting
    ADD CONSTRAINT casting2_actor_4_fkey FOREIGN KEY (actor_4) REFERENCES public.actors(id);


--
-- Name: casting casting2_actor_5_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.casting
    ADD CONSTRAINT casting2_actor_5_fkey FOREIGN KEY (actor_5) REFERENCES public.actors(id);


--
-- Name: casting casting2_actor_6_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.casting
    ADD CONSTRAINT casting2_actor_6_fkey FOREIGN KEY (actor_6) REFERENCES public.actors(id);


--
-- Name: casting casting2_actor_7_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.casting
    ADD CONSTRAINT casting2_actor_7_fkey FOREIGN KEY (actor_7) REFERENCES public.actors(id);


--
-- Name: casting casting2_id_film_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.casting
    ADD CONSTRAINT casting2_id_film_fkey FOREIGN KEY (id_film) REFERENCES public.film_name(id);


--
-- Name: films films_director_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.films
    ADD CONSTRAINT films_director_fkey FOREIGN KEY (director) REFERENCES public.directors(id);


--
-- Name: films films_name_of_film_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.films
    ADD CONSTRAINT films_name_of_film_fkey FOREIGN KEY (name_of_film) REFERENCES public.film_name(id);


--
-- PostgreSQL database dump complete
--

