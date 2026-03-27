import streamlit as st
import streamlit.components.v1 as components 
import textwrap

# --- Función para hacer el scroll suave ---
def auto_scroll_a_id(id_destino):
    components.html(
        f"""
        <script>
            var element = window.parent.document.getElementById("{id_destino}");
            if (element) {{
                // CAMBIAMOS "start" POR "center"
                element.scrollIntoView({{behavior: "smooth", block: "end"}});
            }}
        </script>
        """,
        height=0,
    )

def main():
    if 'total_score' not in st.session_state:
        st.session_state.total_score = 0

    st.markdown("""
        <style>
        div[data-testid="stWidgetLabel"] p {
            font-size: 24px !important;
            font-weight: bold;
            color: #2E86C1;
        }
        </style>
        """, unsafe_allow_html=True)

    st.title("Questionario para relación de parejas")
    st.subheader("Por favor responde a todas las preguntas")

    # 1. Tu pregunta con el tamaño que quieras (h1, h2, h3)


    puntajes ={
        1:"A) Generalmente termina en gritos, silencios prolongados o descalificaciones.",
        2:"B) Evitamos hablar de temas difíciles para no pelear.",
        3:"C) Uno de los dos suele ceder siempre para mantener la paz.",
        4:"D) Hablamos de los problemas, aunque nos cuesta llegar a acuerdos.",
        5:"C) Escuchamos la perspectiva del otro con respeto y buscamos soluciones juntos."
    }
    # pregunta 2


    puntajes_2 ={
        1:"A) El otro suele minimizar el sentimiento o ignorarlo.",
        2:"B) Se genera una discusión sobre quién tiene la culpa del malestar.",
        3:"C) Hay intención de consuelo, pero no sabemos cómo hacerlo efectivamente.",
        4:"D) Solemos ofrecer apoyo, aunque a veces nos gana el estrés personal.",
        5:"E) Existe un espacio seguro donde ambos nos sentimos escuchados y comprendidos."
    }


    puntajes_3 ={
        1:"A) Nos sentimos asfixiados o controlados por el otro..",
        2:"B) Hacemos todo juntos porque no tenemos intereses propios fuera de la relación.",
        3:"C) Vivimos como 'compañeros de piso', apenas compartimos tiempo de calidad.",
        4:"D) Intentamos tener espacios propios, pero a veces genera inseguridad en el otro.",
        5:"E) Respetamos la autonomía individual y disfrutamos genuinamente del tiempo juntos."
    }



    puntajes_4={
        1:"A) Hay sospechas constantes, celos o necesidad de revisar el teléfono del otro.",
        2:"B) La confianza se rompió en el pasado y no hemos podido sanarla.",
        3:"C) Confiamos, pero evitamos profundizar en ciertos temas por miedo a la reacción.",
        4:"D) Sentimos seguridad, aunque a veces surgen dudas por falta de comunicación.",
        5:"E) La confianza es plena y nos sentimos seguros de la lealtad mutua."
    }


    puntajes_5={
        1:"A) Es inexistente; hay una frialdad constante.",
        2:"B) Solo hay afecto cuando uno de los dos busca sexo.",
        3:"C) Es mecánica y poco frecuente, como por compromiso.",
        4:"D) Hay afecto, pero la rutina y el estrés suelen desplazar estos momentos.",
        5:"E) Es una parte esencial y diaria de nuestra conexión."
    }

    puntajes_6={
        1:"A) Solemos culparnos mutuamente por la situación.",
        2:"B) La crisis nos distancia y dejamos de hablar.",
        3:"C) Cada uno intenta resolverlo por su cuenta sin involucrar al otro.",
        4:"D) Nos apoyamos, pero la tensión afecta gravemente el trato entre nosotros.",
        5:"E) Formamos un equipo sólido y enfrentamos la adversidad juntos."
    }

    puntajes_7={   
        1:"A) No tenemos planes en común o son totalmente opuestos.",
        2:"B) Solo planeamos el corto plazo (vacaciones, compras) por miedo al futuro.",
        3:"C) Uno de los dos ha renunciado a sus sueños para seguir los del otro.",
        4:"D) Tenemos metas comunes, pero nos falta un plan claro para alcanzarlas.",
        5:"E) Compartimos valores y una visión de futuro que nos entusiasma a ambos."
    }

    puntajes_8={   
        1:"A) Nula; los errores del pasado se sacan en cara en cada discusión.",
        2:"B) Perdonamos de palabra, pero el resentimiento se nota en el trato.",
        3:"C) Depende de la gravedad del asunto; algunas cosas son tabú.",
        4:"D) Tratamos de perdonar, aunque nos toma mucho tiempo superar las ofensas.",
        5:"E) Aceptamos la humanidad del otro, reparamos el daño y seguimos adelante."
    }

    puntajes_9={  
        1:"A) Como una carga injusta que recae casi totalmente en uno.",
        2:"B) Como una fuente constante de negociación y peleas.",
        3:"C) Se hace lo necesario, pero con mucha desgana y quejas.",
        4:"D) Está repartido, pero la carga mental sigue siendo desigual.",
        5:"E) Como un acuerdo equitativo donde ambos nos sentimos apoyados."
    }

    puntajes_10={  
        1:"A) Casi nunca; el ambiente suele ser tenso o serio.",
        2:"B) Solo cuando estamos con otras personas o en eventos sociales.",
        3:"C) Muy ocasionalmente, la rutina ha consumido el humor.",
        4:"D) Varias veces al mes, cuando logramos desconectar del trabajo.",
        5:"E) Frecuentemente; el humor y el juego son parte de nuestro día a día."
    }

    puntajes_11={  
        1:"A) Muy pobre; siento que ya no conozco a la persona con la que vivo.",
        2:"B) Basado en lo que el otro publica en redes sociales o dice a terceros.",
        3:"C) Superficial; hablamos de logística pero no de emociones.",
        4:"D) Bueno, aunque nos falta actualizar lo que sabemos del otro.",
        5:"E) Profundo; mantenemos conversaciones constantes sobre nuestro mundo interno."
    }

    puntajes_12={    
        1:"A) La discusión no termina hasta que uno 'gana' y el otro se somete.",
        2:"B) Optamos por el 'tratamiento de silencio' durante días.",
        3:"C) Simplemente dejamos de hablar del tema para siempre.",
        4:"D) Aceptamos que pensamos distinto, pero queda una sensación de incomodidad.",
        5:"E) Aceptamos la diferencia con curiosidad y respeto por la individualidad del otro."
    }

    puntajes_13={  
        1:"A) He perdido el respeto y la admiración por mi pareja.",
        2:"B) Me cuesta encontrar cosas que admire en este momento.",
        3:"C) Admiro su rol (como padre/madre/profesional), pero no como persona/pareja.",
        4:"D) Siento admiración, pero rara vez se lo expreso verbalmente.",
        5:"E) Siento un profundo orgullo y se lo demuestro con frecuencia."
    }

    puntajes_14={  
        1:"A) Una fuente de conflicto constante que nos divide.",
        2:"B) Un tema prohibido para evitar explosiones.",
        3:"C) Manejable, pero uno de los dos prioriza a su familia sobre la pareja.",
        4:"D) Ponemos límites, aunque a veces nos cuesta mantenerlos.",
        5:"E) Saludable; la pareja es la prioridad y los límites externos están claros."
    }

    puntajes_15={ 
        1:"A) Definitivamente no lo haría.",
        2:"B) Lo dudaría mucho; quizás buscaría algo diferente.",
        3:"C) Solo si muchas cosas estructurales cambiaran drásticamente.",
        4:"D) Sí, pero con condiciones y límites diferentes desde el inicio.",
        5:"E) Sí, sin duda alguna; volvería a elegir a esta persona."
    }

    st.markdown('<div id="p1"></div>', unsafe_allow_html=True)
    st.markdown("## 1. ¿Cómo describirían la dinámica de comunicación durante un desacuerdo?")

    puntos_pregunta_1 = st.radio(
        "¿Cómo describirían la dinámica de comunicación durante un desacuerdo?",
        options=list(puntajes.keys()),
        format_func=lambda x: puntajes[x],
        index=None,  
        label_visibility="collapsed"
    )

    if puntos_pregunta_1 is not None:
        auto_scroll_a_id("p2")

    st.markdown('<div id="p2"></div>', unsafe_allow_html=True)
    st.markdown("## 2. En cuanto a la validación emocional, cuando uno se siente mal:")
    puntos_pregunta_2 = st.radio(
        "¿Cómo describirían la dinámica de comunicación durante un desacuerdo?", ##este label no se va a ver 
        options=list(puntajes.keys()),
        format_func=lambda x: puntajes_2[x],
        index=None, 
        label_visibility="collapsed"
    )
    if puntos_pregunta_2 is not None:
        auto_scroll_a_id("p3")

    st.markdown('<div id="p3"></div>', unsafe_allow_html=True)
    st.markdown("## 3. ¿Cómo es el equilibrio entre la vida individual y la vida en pareja?")

    puntos_pregunta_3 = st.radio(
        "¿Cómo describirían la dinámica de comunicación durante un desacuerdo?", ##este label no se va a ver 
        options=list(puntajes.keys()),
        format_func=lambda x: puntajes_3[x],
        index=None, 
        label_visibility="collapsed"
    )

    if puntos_pregunta_3 is not None:
        auto_scroll_a_id("p4")

    st.markdown('<div id="p4"></div>', unsafe_allow_html=True)
    st.markdown("## 4. Sobre la confianza y la seguridad en el vínculo:")

    puntos_pregunta_4 = st.radio(
        "¿Cómo describirían la dinámica de comunicación durante un desacuerdo?", ##este label no se va a ver 
        options=list(puntajes.keys()),
        format_func=lambda x: puntajes_4[x],
        index=None, 
        label_visibility="collapsed"
    )

    if puntos_pregunta_4 is not None:
        auto_scroll_a_id("p5")

    st.markdown('<div id="p5"></div>', unsafe_allow_html=True)
    st.markdown("## 5. ¿Qué lugar ocupa la intimidad no sexual (afecto, caricias, complicidad) en su rutina?")

    puntos_pregunta_5 = st.radio(
        "¿Cómo describirían la dinámica de comunicación durante un desacuerdo?", ##este label no se va a ver 
        options=list(puntajes.keys()),
        format_func=lambda x: puntajes_5[x],
        index=None, 
        label_visibility="collapsed"
    )
    if puntos_pregunta_5 is not None:
        auto_scroll_a_id("p6")

    st.markdown('<div id="p6"></div>', unsafe_allow_html=True)
    st.markdown("## 6. Ante una crisis externa (problemas laborales, familiares o económicos):")

    puntos_pregunta_6 = st.radio(
        "¿Cómo describirían la dinámica de comunicación durante un desacuerdo?", ##este label no se va a ver 
        options=list(puntajes.keys()),
        format_func=lambda x: puntajes_6[x],
        index=None, 
        label_visibility="collapsed"
    )
    if puntos_pregunta_6 is not None:
        auto_scroll_a_id("p7")

    st.markdown('<div id="p7"></div>', unsafe_allow_html=True)
    st.markdown("## 7. ¿Cómo perciben su proyecto de vida a largo plazo?")

    puntos_pregunta_7 = st.radio(
        "¿Cómo describirían la dinámica de comunicación durante un desacuerdo?", ##este label no se va a ver 
        options=list(puntajes.keys()),
        format_func=lambda x: puntajes_7[x],
        index=None, 
        label_visibility="collapsed"
    )
    if puntos_pregunta_7 is not None:
        auto_scroll_a_id("p8")

    st.markdown('<div id="p8"></div>', unsafe_allow_html=True)
    st.markdown("## 8. En la resolución de conflictos, la capacidad de perdón es:")

    puntos_pregunta_8 = st.radio(
        "¿Cómo describirían la dinámica de comunicación durante un desacuerdo?", ##este label no se va a ver 
        options=list(puntajes.keys()),
        format_func=lambda x: puntajes_8[x],
        index=None, 
        label_visibility="collapsed"
    )
    if puntos_pregunta_8 is not None:
        auto_scroll_a_id("p9")

    st.markdown('<div id="p9"></div>', unsafe_allow_html=True)
    st.markdown("## 9. El manejo de las responsabilidades (hogar, finanzas, crianza) se siente:")

    puntos_pregunta_9 = st.radio(
        "¿Cómo describirían la dinámica de comunicación durante un desacuerdo?", ##este label no se va a ver 
        options=list(puntajes.keys()),
        format_func=lambda x: puntajes_9[x],
        index=None, 
        label_visibility="collapsed"
    )
    if puntos_pregunta_9 is not None:
        auto_scroll_a_id("p10")
    st.markdown('<div id="p10"></div>', unsafe_allow_html=True)
    st.markdown("## 10. ¿Con qué frecuencia ríen o se divierten genuinamente juntos?")

    puntos_pregunta_10 = st.radio(
        "¿Cómo describirían la dinámica de comunicación durante un desacuerdo?", ##este label no se va a ver 
        options=list(puntajes.keys()),
        format_func=lambda x: puntajes_10[x],
        index=None, 
        label_visibility="collapsed"
    )
    if puntos_pregunta_10 is not None:
        auto_scroll_a_id("p11")
    st.markdown('<div id="p11"></div>', unsafe_allow_html=True)
    st.markdown("## 11. El conocimiento mutuo (saber qué le preocupa al otro, sus sueños actuales) es:")

    puntos_pregunta_11 = st.radio(
        "¿Cómo describirían la dinámica de comunicación durante un desacuerdo?", ##este label no se va a ver 
        options=list(puntajes.keys()),
        format_func=lambda x: puntajes_11[x],
        index=None, 
        label_visibility="collapsed"
    )
    if puntos_pregunta_11 is not None:
        auto_scroll_a_id("p12")
    st.markdown('<div id="p12"></div>', unsafe_allow_html=True)
    st.markdown("## 12. Cuando hay una diferencia de opinión irreconciliable:")

    puntos_pregunta_12 = st.radio(
        "¿Cómo describirían la dinámica de comunicación durante un desacuerdo?", ##este label no se va a ver 
        options=list(puntajes.keys()),
        format_func=lambda x: puntajes_12[x],
        index=None, 
        label_visibility="collapsed"
    )
    if puntos_pregunta_12 is not None:
        auto_scroll_a_id("p13")
    st.markdown('<div id="p13"></div>', unsafe_allow_html=True)
    st.markdown("## 13. ¿Cómo describirían la admiración hacia su pareja?")

    puntos_pregunta_13 = st.radio(
        "¿Cómo describirían la dinámica de comunicación durante un desacuerdo?", ##este label no se va a ver 
        options=list(puntajes.keys()),
        format_func=lambda x: puntajes_13[x],
        index=None, 
        label_visibility="collapsed"
    )
    if puntos_pregunta_13 is not None:
        auto_scroll_a_id("p14")
    st.markdown('<div id="p14"></div>', unsafe_allow_html=True)
    st.markdown("## 14. El impacto de la familia de origen (suegros, cuñados) en la relación es:")

    puntos_pregunta_14 = st.radio(
        "¿Cómo describirían la dinámica de comunicación durante un desacuerdo?", ##este label no se va a ver 
        options=list(puntajes.keys()),
        format_func=lambda x: puntajes_14[x],
        index=None, 
        label_visibility="collapsed"
    )
    if puntos_pregunta_14 is not None:
        auto_scroll_a_id("p15")
    st.markdown('<div id="p15"></div>', unsafe_allow_html=True)
    st.markdown("## 15. Si hoy tuvieran que decidir empezar la relación de nuevo, sabiendo todo lo que saben:")
    puntos_pregunta_15 = st.radio(
        "¿Cómo describirían la dinámica de comunicación durante un desacuerdo?", ##este label no se va a ver 
        options=list(puntajes.keys()),
        format_func=lambda x: puntajes_15[x],
        index=None, 
        label_visibility="collapsed"
    )

    

    if st.button("Calcular Resultado"):
        respuestas = [
            puntos_pregunta_1, puntos_pregunta_2, puntos_pregunta_3,
            puntos_pregunta_4, puntos_pregunta_5, puntos_pregunta_6,
            puntos_pregunta_7, puntos_pregunta_8, puntos_pregunta_9,
            puntos_pregunta_10, puntos_pregunta_11, puntos_pregunta_12,
            puntos_pregunta_13, puntos_pregunta_14, puntos_pregunta_15 
        ]
        

        st.markdown('<div id="seccion-resultado"></div>', unsafe_allow_html=True)
        

        if None in respuestas:
            st.error("⚠️ Por favor responde a todas las preguntas para optener una calificación")
            st.stop()
        else:
            st.session_state.total_score = sum(respuestas)     
            st.write(f"Tu puntaje total es: {st.session_state.total_score}")
            if st.session_state.total_score <= 30:
                st.error("Fase de Alerta Crítica (Intervención Necesaria)")                       
                mensaje_largo = """
                Feedback: La relación muestra signos de un desgaste **profundo** y dinámicas que pueden ser dañinas para ambos.
                La desconexión emocional y el conflicto no resuelto son predominantes. 
                Se recomienda encarecidamente buscar acompañamiento profesional de un psicólogo clínico especializado en parejas para evaluar 
                la viabilidad del vínculo y sanar las heridas acumuladas.
                """
                mensaje_largo = mensaje_largo.strip()
                st.markdown(f"""   
                    <div style="font-size: 24px; line-height: 1.6;">
                        {mensaje_largo}
                    </div>
                    """, unsafe_allow_html=True)

            elif 31 <= st.session_state.total_score <= 45:
                st.warning("Fase de Desgaste Relacional (Riesgo Moderado)")
                mensaje_largo = """
                Feedback: Existen cimientos sobre los cuales trabajar, pero la rutina, 
                la falta de comunicación asertiva o los problemas no resueltos están erosionando la satisfacción. 
                Es un momento preventivo ideal para iniciar terapia de pareja o talleres de comunicación 
                antes de que el resentimiento se vuelva crónico.
                """
                mensaje_largo = mensaje_largo.strip()
                st.markdown(f"""   
                    <div style="font-size: 24px; line-height: 1.6;">
                        {mensaje_largo}
                    </div>
                    """, unsafe_allow_html=True)
            elif 46 <= st.session_state.total_score <= 60:
                st.balloons() # Lluvia de globos
                st.success("Vínculo Estable con Áreas de Mejora")
                mensaje_largo = """
                Feedback: Poseen una relación sólida y saludable en la mayoría de los aspectos. 
                Como toda pareja, enfrentan retos, pero cuentan con las herramientas básicas para mantenerse unidos. 
                El enfoque debe ser potenciar la intimidad y no descuidar los pequeños 
                detalles que alimentan la conexión diaria.
                """
                mensaje_largo = mensaje_largo.strip()
                st.markdown(f"""   
                    <div style="font-size: 24px; line-height: 1.6;">
                        {mensaje_largo}
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.balloons() # Lluvia de globos
                st.success("Conexión Excepcional (Resiliencia Alta)")
                mensaje_largo = """
                Feedback: Su relación se caracteriza por una alta inteligencia emocional, respeto mutuo y una amistad profunda. 
                Han logrado construir un "sistema de seguridad" sólido frente a las crisis. 
                El reto aquí es mantener esta vitalidad a través de los años y seguir creciendo como individuos dentro del proyecto común.
                """
                mensaje_largo = mensaje_largo.strip()
                st.markdown(f"""   
                    <div style="font-size: 24px; line-height: 1.6;">
                        {mensaje_largo}
                    </div>
                    """, unsafe_allow_html=True)
    
        # 4. EL TRUCO MÁGICO: Scroll automático al ancla
        components.html(
            f"""
            <script>
                var element = window.parent.document.getElementById("seccion-resultado");
                if (element) {{
                    element.scrollIntoView({{behavior: "smooth"}});
                }}
            </script>
            """,
            height=0, # Para que el componente no ocupe espacio visual
        )


if __name__ == '__main__':
    main()
