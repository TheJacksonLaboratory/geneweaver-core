"""Cons Stings for testing the PubMed Publication Module."""

EXAMPLE_PARTIAL_XML_RESPONSES = [
    ("<root><data>Some data</data></root>", ("data",)),
    ("<root><error>Some error</error></root>", ("error",)),
    ("<root><PubmedArticle>Some article</PubmedArticle></root>", ("PubmedArticle",)),
    (
        "<root><PubmedArticle><MedlineCitation>"
        "Some citation"
        "</MedlineCitation></PubmedArticle></root>",
        ("PubmedArticle", "MedlineCitation"),
    ),
    (
        "<root><PubmedArticle><MedlineCitation><PMID>"
        "12345678"
        "</PMID></MedlineCitation></PubmedArticle></root>",
        ("PubmedArticle", "MedlineCitation", "PMID"),
    ),
    (
        "<root><PubmedArticle><MedlineCitation><DateCreated>"
        "2023-07-10"
        "</DateCreated></MedlineCitation></PubmedArticle></root>",
        ("PubmedArticle", "MedlineCitation", "DateCreated"),
    ),
    (
        "<root><PubmedArticle><MedlineCitation><Article>"
        "Some article"
        "</Article></MedlineCitation></PubmedArticle></root>",
        ("PubmedArticle", "MedlineCitation", "Article"),
    ),
    (
        "<root><PubmedArticle><MedlineCitation><Article><Journal>"
        "Some journal"
        "</Journal></Article></MedlineCitation></PubmedArticle></root>",
        ("PubmedArticle", "MedlineCitation", "Article", "Journal"),
    ),
    (
        "<root><PubmedArticle><MedlineCitation><Article><JournalIssue>"
        "Some issue"
        "</JournalIssue></Article></MedlineCitation></PubmedArticle></root>",
        ("PubmedArticle", "MedlineCitation", "Article", "JournalIssue"),
    ),
    (
        "<root><PubmedArticle><MedlineCitation><Article><ArticleTitle>"
        "Some title"
        "</ArticleTitle></Article></MedlineCitation></PubmedArticle></root>",
        ("PubmedArticle", "MedlineCitation", "Article", "ArticleTitle"),
    ),
    (
        "<root><PubmedArticle><MedlineCitation><Article><Abstract>"
        "Some abstract"
        "</Abstract></Article></MedlineCitation></PubmedArticle></root>",
        ("PubmedArticle", "MedlineCitation", "Article", "Abstract"),
    ),
    (
        "<root><PubmedArticle><MedlineCitation><Article><AuthorList>"
        "Some author"
        "</AuthorList></Article></MedlineCitation></PubmedArticle></root>",
        ("PubmedArticle", "MedlineCitation", "Article", "AuthorList"),
    ),
    (
        "<root><PubmedArticle><MedlineCitation><Article><Language>"
        "eng"
        "</Language></Article></MedlineCitation></PubmedArticle></root>",
        ("PubmedArticle", "MedlineCitation", "Article", "Language"),
    ),
    (
        "<root><PubmedArticle><MedlineCitation><Article><PublicationTypeList>"
        "Journal Article"
        "</PublicationTypeList></Article></MedlineCitation></PubmedArticle></root>",
        ("PubmedArticle", "MedlineCitation", "Article", "PublicationTypeList"),
    ),
    (
        "<root><PubmedArticle><MedlineCitation><PubmedData>"
        "Some data"
        "</PubmedData></MedlineCitation></PubmedArticle></root>",
        ("PubmedArticle", "MedlineCitation", "PubmedData"),
    ),
]

EXAMPLE_FULL_XMLS = [
    """
    <root>
    <ArticleTitle>Title1</ArticleTitle>
    <AbstractText>Abstract1</AbstractText>
    <Journal><Title>Journal1</Title></Journal>
    <Volume>Vol1</Volume>
    <MedlinePgn>Pgn1</MedlinePgn>
    <PubDate><Year>2022</Year>
    <Month>12</Month>
    <Day>25</Day>
    </PubDate>
    <AuthorList>
    <Author><ForeName>John</ForeName><LastName>Doe</LastName></Author>
    </AuthorList></root>
    """.strip(),
    """
    <root>
    <ArticleTitle>Title2</ArticleTitle>
    <AbstractText>Abstract2</AbstractText>
    <Journal><Title>Journal2</Title></Journal>
    <Volume>Vol2</Volume>
    <MedlinePgn>Pgn2</MedlinePgn>
    <PubDate><Year>2023</Year>
    <Month>1</Month>
    <Day>1</Day>
    </PubDate>
    <AuthorList>
    <Author><ForeName>Jane</ForeName><LastName>Doe</LastName></Author>
    </AuthorList>
    </root>
    """.strip(),
]

EXAMPLE_FULL_XMLS_EXPECTED = [
    {
        "title": "Title1",
        "abstract": "Abstract1",
        "journal": "Journal1",
        "volume": "Vol1",
        "pages": "Pgn1",
        "year": "2022",
        "month": "12",
        "day": "25",
        "authors": ["John Doe"],
    },
    {
        "title": "Title2",
        "abstract": "Abstract2",
        "journal": "Journal2",
        "volume": "Vol2",
        "pages": "Pgn2",
        "year": "2023",
        "month": "1",
        "day": "1",
        "authors": ["Jane Doe"],
    },
]

EXAMPLE_AUTHORS_LIST = [
    "<AuthorList CompleteYN='Y'></AuthorList>",
    "<AuthorList CompleteYN='N'></AuthorList>",
    "<AuthorList></AuthorList>",
    "<AuthorList CompleteYN=''></AuthorList>",
    # The AuthorList node usually has content in it
    "<AuthorList CompleteYN='Y'><Author></Author></AuthorList>",
    "<AuthorList CompleteYN='N'><Author></Author></AuthorList>",
    "<AuthorList><Author></Author></AuthorList>",
    "<AuthorList CompleteYN=''><Author></Author></AuthorList>",
    # The function should work even if we pass it a node that is not an AuthorList.
    "<NotAuthorList CompleteYN='Y'></NotAuthorList>",
    "<NotAuthorList CompleteYN='N'></NotAuthorList>",
    "<NotAuthorList></NotAuthorList>",
    "<NotAuthorList CompleteYN=''></NotAuthorList>",
    "<OtherNode CompleteYN='Y'></OtherNode>",
    "<OtherNode CompleteYN='N'></OtherNode>",
    "<OtherNode></OtherNode>",
    "<OtherNode CompleteYN=''></OtherNode>",
]

EXAMPLE_AUTHORS = [
    (
        "<author><ForeName>Jane</ForeName>" "<LastName>Smith</LastName></author>",
        "Jane Smith",
    ),
    ("<author><LastName>Smith</LastName></author>", "Smith"),
    ("<author><ForeName>Jane</ForeName></author>", "Jane"),
    (
        "<author><ForeName>Jane</ForeName>"
        "<Initials>JS</Initials><LastName>Smith</LastName></author>",
        "Jane Smith",
    ),
    ("<author><Initials>JS</Initials><LastName>Smith</LastName></author>", "JS Smith"),
    ("<author><ForeName></ForeName><LastName>Smith</LastName></author>", "Smith"),
    ("<author><ForeName>Jane</ForeName><LastName></LastName></author>", "Jane"),
    ("<author><ForeName></ForeName><LastName></LastName></author>", ""),
    ("<author><Initials>JS</Initials><LastName></LastName></author>", "JS"),
    ("<author><ForeName>Jane</ForeName><Initials>JS</Initials></author>", "Jane"),
    (
        "<author><LastName>Smith</LastName>" "<ForeName>Jane</ForeName></author>",
        "Jane Smith",
    ),
    (
        "<author><ForeName>Jane</ForeName>"
        "<Initials>JS</Initials><LastName></LastName></author>",
        "Jane",
    ),
    (
        "<author><LastName>Smith</LastName>" "<Initials>JS</Initials></author>",
        "JS Smith",
    ),
    (
        "<author><ForeName>Jane</ForeName>"
        "<Initials></Initials><LastName>Smith</LastName></author>",
        "Jane Smith",
    ),
    (
        "<author><ForeName>Jane</ForeName>"
        "<Initials>JS</Initials><LastName>Smith</LastName></author>",
        "Jane Smith",
    ),
    ("<author><ForeName>John</ForeName><LastName>Doe</LastName></author>", "John Doe"),
    ("<author><LastName>Doe</LastName></author>", "Doe"),
    ("<author><ForeName>John</ForeName></author>", "John"),
    (
        "<author><ForeName>John</ForeName>"
        "<Initials>J</Initials><LastName>Doe</LastName></author>",
        "John Doe",
    ),
    ("<author><Initials>J</Initials><LastName>Doe</LastName></author>", "J Doe"),
    ("<author><ForeName></ForeName><LastName>Doe</LastName></author>", "Doe"),
    ("<author><ForeName>John</ForeName><LastName></LastName></author>", "John"),
    ("<author><ForeName></ForeName><LastName></LastName></author>", ""),
    ("<author><Initials>J</Initials><LastName></LastName></author>", "J"),
    ("<author><ForeName>John</ForeName><Initials>J</Initials></author>", "John"),
    ("<author><LastName>Doe</LastName><ForeName>John</ForeName></author>", "John Doe"),
    (
        "<author><ForeName>John</ForeName>"
        "<Initials>J</Initials><LastName></LastName></author>",
        "John",
    ),
    ("<author><LastName>Doe</LastName><Initials>J</Initials></author>", "J Doe"),
    (
        "<author><ForeName>John</ForeName>"
        "<Initials></Initials><LastName>Doe</LastName></author>",
        "John Doe",
    ),
    (
        "<author><ForeName>John</ForeName>"
        "<Initials>J</Initials><LastName>Doe</LastName></author>",
        "John Doe",
    ),
]


PUBMED_XML_01 = """
<root>
    <PubmedArticle>
        <MedlineCitation Status="Publisher" Owner="NLM">
            <PMID Version="1">12345678</PMID>
            <DateCreated>
                <Year>2023</Year>
                <Month>07</Month>
                <Day>10</Day>
            </DateCreated>
            <Article PubModel="Print">
                <Journal>
                    <ISSN IssnType="Print">1234-5678</ISSN>
                    <JournalIssue CitedMedium="Print">
                        <PubDate>
                            <Year>2023</Year>
                            <Month>Jul</Month>
                        </PubDate>
                    </JournalIssue>
                    <Title>Journal of Something</Title>
                    <ISOAbbreviation>J. Something</ISOAbbreviation>
                    <Volume>7</Volume>
                </Journal>
                <ArticleTitle>A Study about Something.</ArticleTitle>
                <Pagination>
                    <MedlinePgn>1-10</MedlinePgn>
                </Pagination>
                <Abstract>
                    <AbstractText>This study is about something.</AbstractText>
                </Abstract>
                <AuthorList CompleteYN="Y">
                    <Author ValidYN="Y">
                        <LastName>Smith</LastName>
                        <ForeName>John</ForeName>
                        <Initials>JS</Initials>
                    </Author>
                </AuthorList>
                <Language>eng</Language>
                <PublicationTypeList>
                    <PublicationType UI="D016428">Journal Article</PublicationType>
                </PublicationTypeList>
            </Article>
            <PubmedData>
                <History>
                    <PubMedPubDate PubStatus="pubmed">
                        <Year>2023</Year>
                        <Month>7</Month>
                        <Day>10</Day>
                        <Hour>6</Hour>
                        <Minute>0</Minute>
                    </PubMedPubDate>
                </History>
                <ArticleIdList>
                    <ArticleId IdType="pubmed">12345678</ArticleId>
                </ArticleIdList>
            </PubmedData>
        </MedlineCitation>
    </PubmedArticle>
</root>
""".strip()

PUBMED_XML_02 = """
<root>
    <PubmedArticle>
        <MedlineCitation Status="PubMed-not-MEDLINE" Owner="NLM">
            <PMID Version="1">87654321</PMID>
            <DateCreated>
                <Year>2022</Year>
                <Month>11</Month>
                <Day>15</Day>
            </DateCreated>
            <Article PubModel="Print-Electronic">
                <Journal>
                    <ISSN IssnType="Electronic">2345-6789</ISSN>
                    <JournalIssue CitedMedium="Internet">
                        <PubDate>
                            <Year>2022</Year>
                            <Month>Nov</Month>
                        </PubDate>
                    </JournalIssue>
                    <Volume>9</Volume>
                    <Title>Journal of Another Thing</Title>
                    <ISOAbbreviation>J. Another Thing</ISOAbbreviation>
                </Journal>
                <ArticleTitle>Another Study on Something Else.</ArticleTitle>
                <Pagination>
                    <MedlinePgn>100-110</MedlinePgn>
                </Pagination>
                <Abstract>
                    <AbstractText>This study is about something else.</AbstractText>
                </Abstract>
                <AuthorList CompleteYN="Y">
                    <Author ValidYN="Y">
                        <LastName>Doe</LastName>
                        <ForeName>Jane</ForeName>
                        <Initials>JD</Initials>
                    </Author>
                </AuthorList>
                <Language>eng</Language>
                <PublicationTypeList>
                    <PublicationType UI="D016428">Journal Article</PublicationType>
                </PublicationTypeList>
            </Article>
            <PubmedData>
                <History>
                    <PubMedPubDate PubStatus="pubmed">
                        <Year>2022</Year>
                        <Month>11</Month>
                        <Day>15</Day>
                        <Hour>12</Hour>
                        <Minute>0</Minute>
                    </PubMedPubDate>
                </History>
                <ArticleIdList>
                    <ArticleId IdType="pubmed">87654321</ArticleId>
                </ArticleIdList>
            </PubmedData>
        </MedlineCitation>
    </PubmedArticle>
</root>
""".strip()
