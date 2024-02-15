__version__ = "0.1"

import httpx
import pyoxigraph as px


class Ontology:
    def __init__(self, name, uri):
        self.name = name
        self.uri = uri
        self.label = name
        T = {}
        self.graph = px.Store()
        # Retrieve the ontology, parse it and expose some information like descriptions, namespaces etc.
        r = httpx.get(uri)
        if r.status_code == 200:
            self.graph.bulk_load(r.content, "text/turtle")

        first_ontology_found = None

        def get_val(prop):
            return T.get(first_ontology_found, {}).get(prop, [""])[0]

        for s, p, o, _ in self.graph.quads_for_pattern(None, None, None):
            T.setdefault(s.value, {}).setdefault(p.value, []).append(o.value)
            if (
                o.value == "http://www.w3.org/2002/07/owl#Ontology"
                and not first_ontology_found
            ):
                first_ontology_found = s.value

        if not first_ontology_found:
            raise Exception(f"No ontology found in {self.uri}")

        self.label = get_val("http://www.w3.org/2000/01/rdf-schema#label") or self.name
        self.description = get_val("http://purl.org/dc/terms/abstract")

    def __repr__(self):
        return f"Ontology: [{self.name}] {self.label}"


cto = Ontology(
    "cto",
    "https://gitlab.rlp.net/adwmainz/nfdi4culture/knowledge-graph/culture-ontology/-/raw/main/cto.ttl?ref_type=heads",
)
