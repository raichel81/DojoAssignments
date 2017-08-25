// transcribing DNA to RNA to amino acids to codons to 1 letter symbol

// A = U;
// T = A;
// G = C;
// C = G;

// Alanine = A;
// Cysteine = C;
// AsparticAcid = D;
// GlutamicAcid = E;
// Phenylalanine = F;
// Glycine = G;
// Histidine = H;
// Isoleucine = I;
// Lysine = K;
// Leucine = L;
// Methionine = M;
// Asparagine = N;
// Hydroxyproline = O; no codon
// Proline = P;
// Glutamine = Q;
// Arginine = R;
// Serine = S;
// Threonine = T;
// Pyroglutamatic = U; no codon
// Valine = V;
// Tryptophan = W;
// Tyrosine = Y;

codons = {
    A:[GCG,GCA,GCC,GCU],
    C:[UGU,UGC],
    D:[GAC,GAU],
    E:[GAG,GAA],
    F:[UUU,UUC],
    G:[GGU,GGC,GGA,GGG],
    H:[CAU,CAC],
    I:[AUA,AUC,AUU],
    K:[AAG,AAA],
    L:[UUA,UUG],
    M:AUG,
    N:[AAC,AAU],
    P:[CCU,CCC,CCA,CCG],
    Q:[CAA,CAG],
    R:[AGG,AGA],
    S:[AGC,AGU],
    T:[ACG,ACA,ACC,ACU],
    V:[GUG,GUA,GUC,GUU],
    W:UGG,
    Y:[UAU,UAC],
    STOP:[UAA,UAG,UGA]
}

// DECODE AND ENCODE MESSAGES


function dnaToRna(encoded){
    var rnaString = '';
    
    console.log(rnaString);
    return rnaString;
}

dnaToRna("gtactcatgatttgggtgctcgctctcattaaagcataacttacgctgagg");

function rnaToCodon(rnaString){
    var codonArr = [];

    console.log(codonArr);
    return codonArr;
}

rnaToCodon(rnaString);

function codonToLetter(codonArr){
    var decodedString ="";

    console.log(decodedString);
    return decodedString;
}

codonToLetter(codonArr);



every DNA = RNA, 
every 3RNA = codon, 
every codon = Letter 

go through string and make a new string 
every letter change to RNA,

go through newString and send every 3 letters to an Array

increment through array and compare i to the codon object to 
find the key(letter) 
stop === "_"
not found in codon object = ". "
change i to corresponding letter
join array to make string(message)

change 




