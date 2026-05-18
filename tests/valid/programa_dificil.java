public class Main {
    public static void main(String[] args) {
        int capital_inicial = 1000;
        double tasa_interes = 5.5;
        int anos = 3;
        int meta = 1500;
        System.out.println("=== CALCULADORA DE INTERÉS COMPUESTO ===");
        int interes_total = 0;
        int monto_final = capital_inicial;
        int contador = 1;
        while ((contador <= anos)) {
            int interes_anual = (monto_final * ((tasa_interes / 100)));
            int monto_final = (monto_final + interes_anual);
            int interes_total = (interes_total + interes_anual);
        }
        System.out.println("Año:");
        System.out.println(contador);
        System.out.println("Interés del año:");
        System.out.println(interes_anual);
        System.out.println("Monto acumulado:");
        System.out.println(monto_final);
        int contador = (contador + 1);
        System.out.println("=== RESULTADOS FINALES ===");
        System.out.println("Capital inicial:");
        System.out.println(capital_inicial);
        System.out.println("Tasa de interés:");
        System.out.println(tasa_interes);
        System.out.println("Años:");
        System.out.println(anos);
        System.out.println("Interés total generado:");
        System.out.println(interes_total);
        System.out.println("Monto final:");
        System.out.println(monto_final);
        if ((monto_final >= meta)) {
            System.out.println("¡Felicidades! Alcanzaste tu meta de inversión.");
            int excedente = (monto_final - meta);
            System.out.println("Excedente:");
            System.out.println(excedente);
        } else {
            System.out.println("No alcanzaste la meta. Necesitas invertir más.");
            int faltante = (meta - monto_final);
            System.out.println("Faltante:");
            System.out.println(faltante);
        }
        }
        if ((tasa_interes > 0)) {
            int anos_adicionales = (((meta - monto_final)) / ((monto_final * ((tasa_interes / 100)))));
            System.out.println("Años adicionales aproximados:");
            System.out.println(anos_adicionales);
        } else {
            System.out.println("La tasa de interés debe ser mayor a 0");
        }
        }
        int a = 10;
        int b = 3;
        int c = 7;
        int d = 2;
        int resultado1 = ((((a + b)) * c) - d);
        int resultado2 = (((((a * b)) + ((c / d)))) - ((a % b)));
        int resultado3 = (((a > b)) && ((c < d)));
        int resultado4 = (((a <= 10)) || ((b == 3)));
        System.out.println("=== PRUEBAS DE EXPRESIONES ===");
        System.out.println("Resultado 1 (a+b)*c-d:");
        System.out.println(resultado1);
        System.out.println("Resultado 2 ((a*b)+(c/d))-(a%b):");
        System.out.println(resultado2);
        System.out.println("Resultado 3 (a > b) and (c < d):");
        System.out.println(resultado3);
        System.out.println("Resultado 4 (a <= 10) or (b == 3):");
        System.out.println(resultado4);
        int es_rentable = (monto_final > capital_inicial);
        double es_excelente = (monto_final > ((meta * 1.2)));
        if ((es_rentable && es_excelente)) {
            System.out.println("Excelente inversión");
        } else {
            if (es_rentable) {
                System.out.println("Inversión rentable pero no excelente");
            } else {
                System.out.println("Inversión no rentable");
            }
            }
        }
        }
        System.out.println("=== FIN DEL PROGRAMA ===");
    }
}