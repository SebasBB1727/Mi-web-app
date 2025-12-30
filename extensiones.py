from supabase import create_client
#Creamos el enlace con la base de datos en supabase
def inicializar_db():
    client = create_client("https://wkcpobfnenbjmzzwptyd.supabase.co","SupabaseHybridge2028")
    return client
